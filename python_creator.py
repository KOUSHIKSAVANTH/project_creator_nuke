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
os.mkdir(project_name)

for folder in folders:
    os.mkdir(os.path.join(project_name, folder))

print("Project structure created successfully!")