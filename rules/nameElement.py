import ifcopenshell

def specifikElement(model):

    # Vores element, som er en beam
    element = 'IfcBeam'

    # Hent alle elementer af typen 'element' fra modellen
    elements = model.by_type(element)

    # Specifik beam type
    elementName = 'D22-400'

    # Liste til at gemme elementer, der matcher navnet
    num_elements = []

    # Loop igennem hvert element i listen
    for thing in elements:
        # Kontroller, om elementnavnet findes i 'Name'-feltet
        if elementName in thing.Name:
            # Tilføj elementet til listen over fundne elementer
            num_elements.append(thing)

    # Returnér og print antallet af fundne elementer
    print(f"Amount of {elementName}: {len(num_elements)}")


