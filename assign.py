import copy

"""
Hackathon Members:
Leo:    23327987
Sam:    23388986
Ilias:  23361077
Daniel: 23376457
"""

modules = [
    {
        'code': 'CS4222',
        'title': "Software Development",
        'mark': 0,
    },
    {
        'code': 'CS4221',
        'title': "Foundations of Computer Science 1",
        'mark': 0,
    },
    {
        'code': "CS4141",
        'title': "Introduction to Programming",
        'mark': 0,
    }
]


def assign_modules_to_hackathon_members(dictionary):
    for student in dictionary:
        student_modules = copy.deepcopy(modules)
        # Ilias Kourousis
        if student['UID'] == '#23361077':
            student_modules[0]["mark"] = 10
            student_modules[1]["mark"] = 20
            student_modules[2]["mark"] = 30

            student['modules'] = student_modules

        # Daniel Kirwan
        if student['UID'] == '#23376457':
            student_modules[0]["mark"] = 40
            student_modules[1]["mark"] = 50
            student_modules[2]["mark"] = 60

            student['modules'] = student_modules

        # Leo Brady
        if student['UID'] == '#23327987':
            student_modules[0]["mark"] = 70
            student_modules[1]["mark"] = 80
            student_modules[2]["mark"] = 90

            student['modules'] = student_modules

        # Sam Smith
        if student['UID'] == '#23388986':
            student_modules[0]["mark"] = 100
            student_modules[1]["mark"] = 110
            student_modules[2]["mark"] = 120

            student['modules'] = student_modules
