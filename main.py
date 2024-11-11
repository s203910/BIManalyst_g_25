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
from A3.assign_properties import assign_properties
from A3.analyze_cross_section import analyze_cross_sections

# Find stien til 'models'-mappen
models_directory = os.path.join(current_directory, 'models')

# Filnavnet på modellen
model_filename = 'CES_BLD_24_06_STR.ifc'

# Saml hele stien til IFC-filen
model_path = os.path.join(models_directory, model_filename)

# Åbn modellen
model = ifcopenshell.open(model_path)

import ifcopenshell

# Åbn IFC-filen
model = ifcopenshell.open(model_path)


# Kald funktionen
cross_section_overview = analyze_cross_sections(model_path)


"""

cross_sections = [
    (50.0, 270.0, 21000),  # bredde, højde, E-modul
    (25.0, 660.0, 21000)
]

# Kald funktionen
assign_properties(model_path, cross_sections)



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


# Check specifik element
specifikElement(model)
"""
