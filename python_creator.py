import os

project_name = input("Enter the project name: ")

folders = [
    "plates",
    "comp",
    "render",
    "scripts",
    "assets",
    "reference"
]
if os.path.exists(project_name):
    print("project already exists!")
else:
    os.mkdir(project_name)

    for folder in folders:
     os.mkdir(os.path.join(project_name, folder))

    with open(os.path.join(project_name, "README.md"), "w") as file:
     file.write(f"project Name: {project_name}\n")
     file.write("created by: project creator v1.2\n")

    with open(os.path.join(project_name, "notes.txt"), "w") as file:
     file.write("project notes:\n")

     with open(os.path.join(project_name,"comp","shot001.nk"), "w") as file:
      file.write("# Nuke script\n")
      file.write("version 15.0 v1\n")

print("Project structure created successfully!")