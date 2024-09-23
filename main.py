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
from rules.nameElement import specifikElement

# Find stien til 'models'-mappen
models_directory = os.path.join(current_directory, 'models')

# Filnavnet på modellen
model_filename = 'CES_BLD_24_06_STR.ifc'

# Saml hele stien til IFC-filen
model_path = os.path.join(models_directory, model_filename)

# Åbn modellen
model = ifcopenshell.open(model_path)
"""
# Which elements needs to be checked
element = 'IfcBeam'

# Specifik beam type
elementName = 'D22-400'

 Kan du evt. tage med hvis du synes
# Amount required
beams_required = 565

# Check for amount of beams
elementRule(model, element)

# Check if the amount is same as the required amount
amountElement(model, element, beams_required)
"""

# Check specifik element
specifikElement(model)

