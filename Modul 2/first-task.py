import operator

print('\n<<<Kegiatan 1>>>\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Map & Pure Function

def addition(listNumber):
    newListNumber = []
    for number in numbers:
        newListNumber.append(operator.add(number, 2))
    return newListNumber

pureAddition = addition(numbers)
print(f'With Pure Function = {pureAddition}')

# def addition(number):
#     return number + 2

mapAddition = list(map(lambda number: operator.add(number, 2), numbers))
print(f'With Map Function = {mapAddition}\n')

# Filter & Pure Function

def evenNumber(listNumbers):
    newListNumber = []
    for number in listNumbers:
        if number % 2 == 0:
            newListNumber.append(number)
    return newListNumber

pureEvenNumbers = evenNumber(numbers)
print(f'With Pure Function = {pureEvenNumbers}')

filterEvenNumbers = list(filter(lambda number: number % 2 == 0, numbers))
print(f'With Filter Function = {filterEvenNumbers}')

#Robb - Mobile & Web Enthusiast
