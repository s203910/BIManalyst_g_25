import os
import ifcopenshell
import sys

# Få den nuværende sti til 'main.py'
current_directory = os.path.dirname(os.path.abspath(__file__))

# Tilføj 'rules'-mappen til sys.path
sys.path.append(os.path.join(current_directory, 'rules'))

# Henter funktionen fra mappen
from checkRule import beamRule
from checkRule import doorRule

# Find stien til 'models'-mappen
models_directory = os.path.join(current_directory, 'models')

# Filnavnet på modellen
model_filename = 'LLYN - STRU.ifc'

# Saml hele stien til IFC-filen
model_path = os.path.join(models_directory, model_filename)

# Åbn modellen
model = ifcopenshell.open(model_path)

# Eksempel på at få IfcBeam elementer
# things = model.by_type('IfcBeam')
# print(len(things))

# Counting amounts
beamResult = beamRule(model)
doorResult = doorRule(model)

print("Amount of beams in model:", beamResult)
print("Amount of doors in model:", doorResult)