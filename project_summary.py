import json

# project = {
    # "name" : "Kieswerk_Baur",
    # "city" : "Freiburg",
    # "plant_type" : "Kieswerk",
    # "capacity" : 240,
    # "unit":"t/h",
    # "new" : True,
    # "approval": False

# }

def describe_project(project):
    print("Project Summary")
    print("----------------------")
    print(f"Project :{project['name']}")
    print(f"City :{project['city']}")
    print(f"Plant type :{project['plant_type']}")
    print(f"Capacity: {project['capacity']} {project['unit']}")
    if project ["new_installation"]:
        print("The project is a new Installation")
    else:
        print("the project is an existing Installation")
    if project ["approval_identified"]:
        print("Approval status available")
    else:
        print("approval assessment required")

with open("project_data.json", "r") as file:
    project = json.load(file)

describe_project(project)