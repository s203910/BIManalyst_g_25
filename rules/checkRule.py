import ifcopenshell

def beamRule(model):
    beams = model.by_type('IfcBeam')

    result = len(beams)

    return result
