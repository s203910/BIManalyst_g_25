import os
import ifcopenshell
import sys

# Få den nuværende sti til 'main.py'
current_directory = os.path.dirname(os.path.abspath(__file__))

# Tilføj 'rules'-mappen til sys.path
sys.path.append(os.path.join(current_directory, 'rules'))

# Henter funktionen fra mappen
from rules.checkRule import elementRule
from rules.numberElementCheck import amountElement

# Find stien til 'models'-mappen
models_directory = os.path.join(current_directory, 'models')

# Filnavnet på modellen
model_filename = 'LLYN - STRU.ifc'

# Saml hele stien til IFC-filen
model_path = os.path.join(models_directory, model_filename)

# Åbn modellen
model = ifcopenshell.open(model_path)

# Which elements needs to be checked
element = 'IfcBeam'
# Amount required
beams_required = 565

# Check for amount of beams
beamAmount = elementRule(model, element)

# Check if the amount is same as the required amount
amountElement(model, element, beams_required)
