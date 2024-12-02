# **Reflections s203910**
 **Learning Experience**
 At the start of the course I knew how to do basic models in Blender Bonsai from having the course OpenBIM. At the end of the course I knew how to actually read, process and adjust data in an IfcModel without even opening it, with a python script through github.
 Getting more familiar with Ifc - and Python too - would allow me to do just about anything in terms fo modelling through python scripts.

 **Process of developing the tutorial**
 No matter how much I decide to improve at OpenBIM usage later in my studies, the tools I've learnt in this course will allow me to caster read, edit and work with IfcModels for the rest of my studies and career.
 The amount of choice in the use cases was adequate.
 I think the scope of the course was a bit too broad and it would have been a better learning experience to spend a bit more time of the core focuses on the course and less on extra tools / concepts.

 **My future for Advanced use of OpenBIM**
 I will likely use OpenBIM in my thesis if a use case comes up. I do not plan on specializing specifically in OpenBIM use.
 I will likely use OpenBIM in my career if it will improve my efficiency.

 **Wrap up**
 I liked that A1-A5 were tied together and that the whole course felt like a project, while also learning a lot and applying concepts and tools throughout. 
 A3 was an interesting assignment, and while I'm happy with the outcome, due to my limited python experience it was challenging to make something too comprehensive.
 I liked the idea of A4, but it did feel a bit out of place.
 Overall the manager - anaylyst relationsships limits creativity, as managers need to be able to keep tabs on all projects. We "overdid" an early assignment and were asked to tone it down a bit so managers didn't have to do extra work.
 
 

# **Reflection Andreas**
 **Building stage**
 The tool will be used in the design (B) phase, when building models and performing structural analysis.

 **Subject**
 The statics engineers and modellers would use this tool, both to ensure model is correct and read information for the model to ensure structural integrity.

 **Model requirements**
 For the tool to work the model must have IfcBeam's, IfcElementName's, geometrical dimensions on the beams and these must be an IfcMappedItem an IfcExtrudedAreaSolid with an IfcRectagnleProfileDef like in Building#2406. Material properties are not required as the model will identify if these are missing for the IfcBeams and then create these, but if there arent any beams set up in the IfcModel to begin with, the tool does nothing. 