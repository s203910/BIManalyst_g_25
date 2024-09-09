import ifcopenshell

#from .rules import windowRule
#from .rules import doorRule

#Grey model:
#model = ifcopenshell.open(r'C:\Users\thoma\Documents\GitHub\AdvBIM-G25\models\CES_BLD_24_06_STR.ifc')

#Coloured model:
model = ifcopenshell.open(r'C:\Users\thoma\Documents\GitHub\AdvBIM-G25\models\LLYN - STRU.ifc')

print(model)

things = model.by_type('IfcBeam')

print(len(things))

#windowResult = windowRule.checkRule(model)
#doorResult = doorRule.checkRule(model)

#print("Window result:", windowResult)
#print("Door result:", doorResult)