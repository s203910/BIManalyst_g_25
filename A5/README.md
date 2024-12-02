# **Reflections Thomas**
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

# **Reflection Andreas**
**Identify your own level at the beginning of this course and where you ended**
At the beginning, I was definitely a self-learner, having been exposed to the concepts both at work and at university. However, this exposure was limited to some interactions with the concepts of ontology and Molio standards. Over the course, I feel I’ve moved closer to understanding the importance of having a "common language" in OpenBIM, even though I still don’t fully grasp all the standards and terms used.

**What else do you still need to learn?**
I need a deeper dive into the standards to better understand what fully utilizing the OpenBIM concept might entail. At the moment, I don’t think Bonsai is mature enough to be widely implemented in the Danish consulting industry, but the underlying concepts are excellent.

**How you might use OpenBIM in the future?**
I might use it in a work setting, as I already work extensively with FSD, which is close to being an open-source fire CFD program used for simulations in fire engineering. GitHub plays a significant role in this, and internally in our firm, a new standard for naming and BIM usage is being implemented. Some of the knowledge I’ve gained in this course could be useful in that context.

**Did the process of the course enable you to answer or define questions that you might need later for your thesis?**
There is potential to implement the idea of OpenBIM into developing a tool that automatically generates an FSD model from an OpenBIM model. This could be an area worth exploring further.

**Would you have preferred to have been given less choice in the use cases?**
Yes, I would. I would also have preferred the difficulties to be higher. The course, as it stands, is simply too easy, and it feels like everyone is getting a free pass. I understand the intention behind creating an inclusive learning environment, but at a master’s level, it is reasonable to set standards that challenge and require students to develop themselves. A loose structure makes it easy to opt for the simplest solution, which doesn’t necessarily encourage outstanding performance.

**Was the number of tools for the course ok – should we have more or less? If so, which ones would you leave out?**
As mentioned, the course seems to have a very low threshold. I would have liked there to be more material to work through or at least clearer boundaries regarding what is required at different stages of the course. The course is too loosely structured, and I found it challenging to determine what was expected of me at any given time. 

# **Summary of feedback**
**Nice**



