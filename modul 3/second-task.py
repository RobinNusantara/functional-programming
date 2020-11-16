import sys
import pprint
sys.path.insert(1, '/Users/robin/VisualStudioCodeProjects/functional-programming/utils')
from utils_func import printDictInsideList

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

print('<<<Original Dictionary>>>\n')

pprint.pprint(students)
print()

def detectEmptyValue(dictionaries):
    for idx, dictionary in enumerate(dictionaries):
        for key in dictionary:
            if dictionary.get(key) == '':
                print('-------')
                print(f'\n{dictionaries[idx]}')
                print(f'\nWe detected there\'s an empty value in {key} key in dictionary line {idx + 1}\n')
                userInput = input(f'Please input value in {key} key in dictionary line {idx + 1} : ')
                dictionary.update({key: userInput})
    return dictionaries
        
print('\n<<<Modified Dictionary>>>\n')

detectEmptyValue(students)
printDictInsideList(students)

#Robb Mobile & Web Enthusiast
