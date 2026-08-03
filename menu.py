import nuke
import project_creator


def launch_project_creator():

    project_name = nuke.getInput("Project Name", "Demo_Project")

    if not project_name:
        return

    root_path = nuke.getFilename("Choose Project Location", "")

    if not root_path:
        return

    import os
    root_path = os.path.dirname(root_path)

    project_creator.create_project(project_name, root_path)


pipeline_menu = nuke.menu("Nuke").addMenu("Pipeline")

pipeline_menu.addCommand(
    "Create Project",
    launch_project_creator
)