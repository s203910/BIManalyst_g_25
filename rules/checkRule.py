import ifcopenshell

def beamRule(model):
    beams = model.by_type('IfcBeam')

    result = f"Beams: {len(beams)}"

    return result

def doorRule(model):
    doors = model.by_type('IfcDoor')

    result = f"Doors: {len(doors)}"

    return result