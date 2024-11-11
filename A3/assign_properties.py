import ifcopenshell

def assign_properties(model_path, cross_sections):
    """
    Tildeler E-modul, modstandsmoment og inertimoment til IfcBeam-objekter
    baseret på en liste over tværsnitsstørrelser og E-moduler.
    
    Parameters:
    model_path (str): Stien til IFC-modellen.
    cross_sections (list of tuples): Liste af tuples med tværsnitsstørrelser og E-moduler.
                                     Hver tuple er på formen (width, height, e_modulus).
    """
    # Åbn IFC-filen
    model = ifcopenshell.open(model_path)
    
    # Iterer over alle IfcBeam-objekter
    for beam in model.by_type("IfcBeam"):
        representation = beam.Representation
        processed = False  # Flag to track if the beam is processed
        for rep in representation.Representations:
            if rep.RepresentationIdentifier == "Body" and not processed:
                for item in rep.Items:
                    if item.is_a("IfcMappedItem") and not processed:
                        mapped_representation = item.MappingSource.MappedRepresentation
                        for mapped_item in mapped_representation.Items:
                            if mapped_item.is_a("IfcExtrudedAreaSolid") and not processed:
                                profile = mapped_item.SweptArea
                                if profile.is_a("IfcRectangleProfileDef"):
                                    # Afrund bredde og højde til 2 decimaler
                                    width = round(profile.XDim, 2)
                                    height = round(profile.YDim, 2)
                                    
                                    # Tjek om tværsnittet matcher nogen i input-listen
                                    for cross_section in cross_sections:
                                        if (width, height) == cross_section[:2]:
                                            e_modulus = cross_section[2]
                                            
                                            # Tjek om bjælken allerede har de ønskede properties
                                            has_e_modulus = False
                                            has_section_modulus = False
                                            has_moment_of_inertia = False
                                            existing_properties = {}

                                            for rel in beam.IsDefinedBy:
                                                if rel.is_a("IfcRelDefinesByProperties"):
                                                    prop_set = rel.RelatingPropertyDefinition
                                                    if prop_set.is_a("IfcPropertySet"):
                                                        for prop in prop_set.HasProperties:
                                                            if prop.Name == "ElasticModulus":
                                                                has_e_modulus = True
                                                                existing_properties["ElasticModulus"] = prop.NominalValue.wrappedValue
                                                            elif prop.Name == "SectionModulus":
                                                                has_section_modulus = True
                                                                existing_properties["SectionModulus"] = prop.NominalValue.wrappedValue
                                                            elif prop.Name == "MomentOfInertia":
                                                                has_moment_of_inertia = True
                                                                existing_properties["MomentOfInertia"] = prop.NominalValue.wrappedValue
                                            
                                            # Hvis alle properties allerede er til stede, spring bjælken over
                                            if has_e_modulus and has_section_modulus and has_moment_of_inertia:
                                                print(f"Properties allerede tilstede for bjælke ID {beam.id()} Navn: {beam.Name}")
                                                print("Eksisterende properties:")
                                                for prop_name, prop_value in existing_properties.items():
                                                    print(f"  - {prop_name}: {prop_value}")
                                                processed = True
                                                break

                                            # Beregn modstandsmoment og inertimoment
                                            section_modulus = (width * height**2) / 6
                                            moment_of_inertia = (width * height**3) / 12
                                            
                                            # Liste til at gemme de properties, der tilføjes
                                            added_properties = []
                                            
                                            # Opret en property set til de manglende properties
                                            property_set = model.create_entity("IfcPropertySet", Name="StructuralProperties")
                                            rel_defines = model.create_entity("IfcRelDefinesByProperties", RelatingPropertyDefinition=property_set, RelatedObjects=[beam])
                                            
                                            # Opret en midlertidig liste til HasProperties
                                            properties = list(property_set.HasProperties) if property_set.HasProperties else []
                                            
                                            if not has_e_modulus:
                                                e_modulus_property = model.create_entity(
                                                    "IfcPropertySingleValue",
                                                    Name="ElasticModulus",
                                                    NominalValue=model.create_entity("IfcReal", e_modulus)
                                                )
                                                properties.append(e_modulus_property)
                                                added_properties.append(f"ElasticModulus: {e_modulus}")
                                            
                                            if not has_section_modulus:
                                                section_modulus_property = model.create_entity(
                                                    "IfcPropertySingleValue",
                                                    Name="SectionModulus",
                                                    NominalValue=model.create_entity("IfcReal", section_modulus)
                                                )
                                                properties.append(section_modulus_property)
                                                added_properties.append(f"SectionModulus: {section_modulus}")
                                            
                                            if not has_moment_of_inertia:
                                                moment_of_inertia_property = model.create_entity(
                                                    "IfcPropertySingleValue",
                                                    Name="MomentOfInertia",
                                                    NominalValue=model.create_entity("IfcReal", moment_of_inertia)
                                                )
                                                properties.append(moment_of_inertia_property)
                                                added_properties.append(f"MomentOfInertia: {moment_of_inertia}")
                                            
                                            # Tildel den midlertidige liste tilbage til HasProperties
                                            property_set.HasProperties = tuple(properties)
                                            
                                            # Print status med både ID, navn og tilføjede properties
                                            print(f"Properties tilføjet til bjælke ID {beam.id()} Navn: {beam.Name} med tværsnit {width}x{height}")
                                            print("Tilføjede properties:")
                                            for prop in added_properties:
                                                print(f"  - {prop}")
                                            
                                            # Mark the beam as processed to avoid repetition
                                            processed = True
                                            break

