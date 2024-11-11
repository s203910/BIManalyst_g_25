# **About**
 **The problem**
 In order to perform an analysis of the beams in the structural model, certain material properties such as cross section and E-module need to be specified. This information should therefore be available in the model. The tool will check for this information to verify it's presence to ensure that it is added to the model and can be used for further analysis.

 The tool acts as quality control as material properties might not be in the IfcModel, which hinders structural analysis.


 **The tool**
 Description of the tool
 
 Instructions to run the tool

# **Advanced Building Design**
 **Building stage**
 The tool will be used in the design (B) phase, when building models and performing structural analysis.

 **Subject**
 The statics engineers and modellers would use this tool, both to ensure model is correct and read information for the model to ensure structural integrity.

 **Model requirements**
 For the tool to work the model must have IfcBeam's, IfcElementName's and geometrical dimensions on the beams. Material properties are not required as the model will identify if these are missing for the IfcBeams and then create these, but if there arent any beams set up in the IfcModel to begin with, the tool does nothing.