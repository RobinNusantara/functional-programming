students = [
    {
        "firstName": "Afwun",
        "lastName": "Shiddiq",
        "age": 20,
        "gender": "Male"
    },
    {
        "firstName": "Rosalia",
        "lastName": "Benarti",
        "age": 21,
        "gender": "Female"
    },
    {
        "firstName": "Ahmad",
        "lastName": "Sentosa",
        "age": 20,
        "gender": "Male"
    },
    {
        "firstName": "Mary",
        "lastName": "Jane",
        "age": 19,
        "gender": "Female"
    },
    {
        "firstName": "Muhammad",
        "lastName": "Jito",
        "age": 27,
        "gender": "Male"
    },
    {
        "firstName": "Bunga",
        "lastName": "Lestari",
        "age": 26,
        "gender": "Female"
    },
]

def sortList(func):
    def listToSort(_list, key):
        _list.sort(key=lambda _dict: _dict.get(key))
        return func(_list, key)
    return listToSort

@sortList
def printStudents(students, key):
    for student in students:
        name = student.get("firstName") + student.get("lastName")
        print(f'Mr {name}' if student.get('gender') == 'Male' else f'Ms {name}')
        
printStudents(students, 'age')

#Robb Mobile & Web Enthusiast
