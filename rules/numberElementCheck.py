import ifcopenshell

def amountElement(model, element, amount):
    elementAmount = model.by_type(element)

    if len(elementAmount) == amount:
        print(f'The number of {element}s is correct')
    else:
        print(f'The number of {element}s is incorrect')