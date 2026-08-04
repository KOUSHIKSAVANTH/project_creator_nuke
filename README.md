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

![Pipeline Menu](screenshots/pipeline.png.png)

### Create Project Popup

![Create Project Popup](screenshots/create_project.png.png)

---

## create project name

![naming the project](screenshots/project_name.png.png)

## project creation

![project created successfully](screenshots/project_creation.png.png)

## Folder structure

![folder structure](screenshots/folder_structure.png.png)

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