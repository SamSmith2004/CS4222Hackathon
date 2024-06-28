import numpy as np

def top_five_students(dict, module_name):
    leaderboard = {}

    for student in dict:
        if 'modules' in student:
            leaderboard[student['First Name'] + ' ' + student['Last Name']] = 0

            for module in student['modules']:
                if module['code'] == module_name:
                   leaderboard[student['First Name'] + ' ' + student['Last Name']] = module['mark']

    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

    print(f'{module_name}', sorted_leaderboard[0:3])