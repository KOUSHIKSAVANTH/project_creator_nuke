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

print("Project structure created successfully!")