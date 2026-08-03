import os
import json
import nuke


def create_project(project_name, root_path):

    project_path = os.path.join(root_path, project_name)

    if os.path.exists(project_path):
        nuke.message("Project already exists!")
        return

    with open(os.path.join(os.path.dirname(__file__), "config.json"), "r") as config:
        data = json.load(config)

    folders = data["folders"]

    # Create project folder
    os.mkdir(project_path)

    # Create subfolders
    for folder in folders:
        os.mkdir(os.path.join(project_path, folder))

    # README
    with open(os.path.join(project_path, "README.md"), "w") as file:
        file.write(f"Project Name : {project_name}\n")
        file.write("Pipeline Tool Version : 2.0\n")

    # Notes
    with open(os.path.join(project_path, "notes.txt"), "w") as file:
        file.write("Project Notes\n")

    # Nuke script
    nk_file = os.path.join(project_path, "comp", "shot001.nk")

    with open(nk_file, "w") as file:
        file.write("# Nuke Script\n")
        file.write("version 15.0 v1\n")

    nuke.message(f"Project '{project_name}' created successfully!")