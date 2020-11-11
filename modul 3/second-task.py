import sys
sys.path.insert(1, '/Users/robin/VisualStudioCodeProjects/functional-programming/utils')
from utils import printDictInsideList

print('\n<<<Original Dictionary>>>\n')

students = [
    {
        'studentName': 'Ahmad',
        'studentDepartment': 'Informatika',
        'studentSemester': 2,
        'studentGeneration': '',
    },
    {
        'studentName': '',
        'studentDepartment': 'Pertanian',
        'studentSemester': '',
        'studentGeneration': 2017,
    },
    {
        'studentName': 'Insan',
        'studentDepartment': '',
        'studentSemester': 3,
        'studentGeneration': '',
    },
    {
        'studentName': 'Malik',
        'studentDepartment': '',
        'studentSemester': 6,
        'studentGeneration': 2018,
    },
    {
        'studentName': '',
        'studentDepartment': 'Kehutanan',
        'studentSemester': '',
        'studentGeneration': 2015,
    },
]

for idx, student in enumerate(students):
    for key in student:
        if student[key] == '':
            userInput = input(f'Input value {key} in {idx} : ')
            student.update({key: userInput})

print('\n<<<Modified Dictionary>>>\n')

printDictInsideList(students)

#Robb Mobile & Web Enthusiast
