# Installing in Nuke

## Step 1

Copy the folder:

```text
nuke_pipeline_tool
```

to:

```text
C:\Users\YOUR_NAME\.nuke\
```

## Step 2

Edit `.nuke/menu.py`:

```python
nuke.pluginAddPath("./python_project_creator/nuke_integration")
```

## Step 3

Restart Nuke.

You will see:

```text
Pipeline → Create Project
```