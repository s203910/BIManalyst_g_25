import ifcopenshell
from collections import defaultdict

def analyze_cross_sections(model_path):
    """
    Gennemgår IfcBeam-objekter og returnerer en oversigt over unikke tværsnitstørrelser,
    antal bjælker pr. størrelse, og antal bjælker uden de nødvendige properties.

    Parameters:
    model_path (str): Stien til IFC-modellen.
    
    Returns:
    dict: En dictionary med tværsnitstørrelser som nøgler og antal bjælker, antal uden properties som værdier.
    """
    # Åbn IFC-filen
    model = ifcopenshell.open(model_path)
    
    # Dictionary til at holde styr på tværsnitstørrelser og bjælketælling
    cross_section_summary = defaultdict(lambda: {"total_count": 0, "missing_properties_count": 0})

    # Iterer over alle IfcBeam-objekter
    for beam in model.by_type("IfcBeam"):
        representation = beam.Representation
        for rep in representation.Representations:
            if rep.RepresentationIdentifier == "Body":
                for item in rep.Items:
                    if item.is_a("IfcMappedItem"):
                        mapped_representation = item.MappingSource.MappedRepresentation
                        for mapped_item in mapped_representation.Items:
                            if mapped_item.is_a("IfcExtrudedAreaSolid"):
                                profile = mapped_item.SweptArea
                                if profile.is_a("IfcRectangleProfileDef"):
                                    # Afrund bredde og højde til 2 decimaler for at få tværsnitstørrelsen
                                    width = round(profile.XDim, 2)
                                    height = round(profile.YDim, 2)
                                    cross_section_key = (width, height)
                                    
                                    # Opdater total count for denne tværsnitstørrelse
                                    cross_section_summary[cross_section_key]["total_count"] += 1
                                    
                                    # Tjek om bjælken mangler de ønskede properties
                                    has_e_modulus = False
                                    has_section_modulus = False
                                    has_moment_of_inertia = False
                                    
                                    for rel in beam.IsDefinedBy:
                                        if rel.is_a("IfcRelDefinesByProperties"):
                                            prop_set = rel.RelatingPropertyDefinition
                                            if prop_set.is_a("IfcPropertySet"):
                                                for prop in prop_set.HasProperties:
                                                    if prop.Name == "ElasticModulus":
                                                        has_e_modulus = True
                                                    elif prop.Name == "SectionModulus":
                                                        has_section_modulus = True
                                                    elif prop.Name == "MomentOfInertia":
                                                        has_moment_of_inertia = True
                                    
                                    # Hvis bjælken mangler en eller flere properties, opdater tællingen
                                    if not (has_e_modulus and has_section_modulus and has_moment_of_inertia):
                                        cross_section_summary[cross_section_key]["missing_properties_count"] += 1
    
    # Print oversigt
    print("Tværsnitsstørrelser og bjælkeoplysninger:")
    for (width, height), counts in cross_section_summary.items():
        print(f"Tværsnit {width}x{height} mm:")
        print(f"  - Total antal bjælker: {counts['total_count']}")
        print(f"  - Antal uden nødvendige properties: {counts['missing_properties_count']}")
    
    return cross_section_summary
