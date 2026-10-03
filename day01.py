name = "Yahya"
career = "Civil Engineering"
direction = "AI + Infrastructure"
experience_years = 2
learning_hours_week = 12
building_startup = True

#print(type(name))
#print(type(experience_years))
#print(type(building_startup))

goals = [
    "Learn Python",
    "Build BImSchG-AI",
    "Learn APIs",
    "Learn document AI",
    "Build useful AI products"
]
#print(goals[0])
#print(goals[1])

goals.append("get first paying customer")

#print(goals[5])

anlage = {
    "name": "Asphaltmischanlage Freiburg",
    "type": "Asphalt Plant",
    "capacity": 240,
    "unity":"t/h",
    "location": "Baden-Württemberg",
    "new_installation": True
}

#print(anlage["name"])
#print(anlage["capacity"])

project = {
    "project name":"EU K4946",
    "city": "Mullheim",
    "plan type":"AP",
    "capacity": 240,
    "capacity unit":"t/h",
    "neue Anlage": True,
    "approved": False,       
}

#print(f"Project: {project['project name']}")
#print(f"Location: {project['city']}")
#print(f"Capacity: {project['capacity']} {project['capacity unit']} ")
#print(f"Approval identified: {project['approved']}")


def describe_project(project):
    print(f"Project: {project['project name']}")
    print(f"Location: {project['city']}")
    print(f"Capacity: {project['capacity']} {project['capacity unit']} ")
    print(f"Approval identified: {project['approved']}")

#describe_project(project)