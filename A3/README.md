# **About**
 **The problem**
 In order to perform an analysis of the beams in the structural model, certain material properties such as cross section and E-module need to be specified. This information should therefore be available in the model.

 **The tool**
 The tool will check for this information to verify it's presence to ensure that it is added to the model and can be used for further analysis. Material properties do not exist, the tool can add these for each specific beam type, classified by cross section.

 The tool acts as quality control as material properties might not be in the IfcModel, which hinders structural analysis. 

 The script consists of `main.py` which calls 2 different functions `analyze_cross_sections(model_path)` and `assign_properties(model_path, cross_sections)`.
 
 In order to run the tool, one must do the following:
 1. Ensure that the `main.py` can access the model.
 2. Input the model name in the `main.py`.
 3. Call the function `analyze_cross_sections(model_path)`.
 4. See which beams are missing E-module, moment of inertia and moment of resistance.
 5. If material properties should be assigned for a group of beams with a certain cross section, fill in (with,height,E_module) under `cross_section` in `main.py`, and call the function `assign_properties(model_path, cross_sections)`.
 6. (Repeat step 3 to confirm result).

# **Advanced Building Design**
 **Building stage**
 The tool will be used in the design (B) phase, when building models and performing structural analysis.

 **Subject**
 The statics engineers and modellers would use this tool, both to ensure model is correct and read information for the model to ensure structural integrity.

 **Model requirements**
 For the tool to work the model must have IfcBeam's, IfcElementName's, geometrical dimensions on the beams and these must be an IfcMappedItem an IfcExtrudedAreaSolid with an IfcRectagnleProfileDef like in Building#2406. Material properties are not required as the model will identify if these are missing for the IfcBeams and then create these, but if there arent any beams set up in the IfcModel to begin with, the tool does nothing. 