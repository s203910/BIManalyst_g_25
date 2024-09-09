import ifcopenshell

#from .rules import beamRule
#from .rules import doorRule

#Grey model:
#model = ifcopenshell.open(r'C:\Users\thoma\Documents\GitHub\AdvBIM-G25\models\CES_BLD_24_06_STR.ifc')

#Coloured model:
model = ifcopenshell.open(r'C:\Users\thoma\Documents\GitHub\AdvBIM-G25\models\LLYN - STRU.ifc')

print(model)

things = model.by_type('IfcBeam')

print(len(things))

beamResult = beamRule.checkRule(model)
#doorResult = doorRule.checkRule(model)

print("Amount of beams in model:", beamResult)
#print("Door result:", doorResult)