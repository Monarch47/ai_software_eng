from file_writing import write_to_text_file
from datetime import datetime
from file_read import read_file
import researcher
import planning

# Time stamp
def current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

print("Hey!, Lagrangian this side")

# directory selection
folder_path = input("Folder directory for the project: ")
project_name = input("Enter the project name: ")
text_to_write = f"""Project Name: {project_name},
Date and time of initialisation: {current_time}"""
write_to_text_file(folder_path, project_name, text_to_write)

# Context to understand the project
print("I will ask few quesitons regarding the project")
tech_ans = input("Specific tech stack yes[Y]/no[N]")
design_ans = input("Specific design yes[Y]/no[N]")
tech = "Best tech stack for the project"
design = "Best design theme for the project"
prd_type = input("Product type: ")
if tech_ans == "N":
    tech = input("Tech Stack if required specific: ")
else:
    pass
if design_ans == "N":
    design = input("Design theme: ")
else:
    pass

funtionalities = input("Tell the functionality: ")
features = input("Tell must have features: ")

file_name = "product_structure.txt"
text_to_write = f"""Product Type: {prd_type},
tech stack: {tech},
design: {design},
functionalities: {funtionalities},
features: {features}
Date and time of initialisation: {current_time}"""
write_to_text_file(folder_path, file_name, text_to_write)

#researching
prompt_research = read_file(folder_path, file_name)
response = researcher.research(prompt_research)
researcher_text = "research.txt"
write_to_text_file(folder_path,researcher_text,response)

#planning tech stuff
prompt_planning = read_file(folder_path,researcher_text)
response = planning.planning(prompt_planning)
planning_text = "planning.txt"
write_to_text_file(folder_path,planning_text,response)











