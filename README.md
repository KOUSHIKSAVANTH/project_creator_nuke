# Python Project Creator for Nuke

A simple pipeline tool that creates a VFX project folder structure directly from inside **Nuke**.

---

## Features

- Create project folders automatically
- Generate `README.md` and `notes.txt`
- Create a starter `.nk` file
- Launch from **Nuke → Pipeline → Create Project**
- Uses **Python + Nuke API**

---

## Nuke Integration

### Pipeline Menu

![Pipeline Menu](screenshots/pipeline.png)

### Create Project Popup

![Create Project Popup](screenshots/create_project.png)

---

## create project name

![naming the project](screenshots/project_name.png)

## project creation

![project created successfully](screenshots/project_creation.png)

## Folder structure

![folder structure](screenshots/folder_structure.png)

## practice code

![practice code 1](screenshots/practice_code1.png)

![practice code 2](screenshots/practice_code2.txt)

![practice code 3](screenshots/practice_code3.txt)

---

## Project Structure

```text
python_project_creator/
│
├── project_creator.py
├── config.json
├── README.md
├── screenshots/
│   ├── nuke_menu.png
│   ├── create_project_popup.png
│   └── generated_folders.png
└── nuke_integration/
    ├── menu.py
    └── install_in_nuke.txt
```