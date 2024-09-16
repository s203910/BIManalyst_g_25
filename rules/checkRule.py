import ifcopenshell

def elementRule(model, element):
    elements = model.by_type(element)

    result = len(elements)

    return print(f'The amounts of {element} is {result}')
