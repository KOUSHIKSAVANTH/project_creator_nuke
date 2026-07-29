import os

def create_folders(project_name,folders):
    os.mkdir(project_name)

    for folder in folders:
        os.mkdir(os.oath.join(project_name,folder))

def create_readme(project_name):
    with open(os.path.join(project_name, "README.md"), "w") as file:
        file.write(f"project name: {project_name}\n")
        file.write(f"created by: project creator\n")

def create_notes(project_name):
    with open(os.path.join(project_name, "notes.txt"), "w")as file:
        file.write("project notes\n")

def create_nuke(project_name):
    with open(os.path.join(project_name, "comp","shot001.nk"), "w") as file:
        file.write("# nuke script\n")
        file.write("version 15.0 v1\n")


folders = ["plates","comp", "renders","scripts","assets","reference"]

project_name = input("Enter the project name: ")

if os.path.exists(project_name):
    print("Project already exists.")

else:
    create_folders(project_name,folders)
    create_readme(project_name)
    create_notes(project_name)
    create_nuke(project_name)

    print("project structure created successfully!")

