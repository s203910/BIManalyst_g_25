import os
import ifcopenshell

#from .rules import beamRule
#from .rules import doorRule

#Grey model:
#model = ifcopenshell.open(r'C:\Users\thoma\Documents\GitHub\AdvBIM-G25\models\CES_BLD_24_06_STR.ifc')

#Coloured model:
# Få den nuværende sti til 'main.py'
current_directory = os.path.dirname(os.path.abspath(__file__))

# Find stien til 'models'-mappen
models_directory = os.path.join(current_directory, 'models')

# Filnavnet på modellen
model_filename = 'LLYN - STRU.ifc'

# Saml hele stien til IFC-filen
model_path = os.path.join(models_directory, model_filename)

# Åbn modellen
model = ifcopenshell.open(model_path)

print(model)

# Eksempel på at få IfcBeam elementer
things = model.by_type('IfcBeam')
print(len(things))

beamResult = beamRule.checkRule(model)
#doorResult = doorRule.checkRule(model)

print("Amount of beams in model:", beamResult)
#print("Door result:", doorResult)