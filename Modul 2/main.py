import operator

print('\n<<<Kegiatan 1>>>\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Map & Pure Function

def addition(listNumber):
    newListNumber = []
    for number in numbers:
        newListNumber.append(number + 2)
    return newListNumber

pureAddition = addition(numbers)
print(f'With Pure Function = {pureAddition}')

# def addition(number):
#     return number + 2

mapAddition = list(map(lambda number: number + 2, numbers))
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

print('\n<<<Kegiatan 2>>>\n')

firstList = ['jurusan', 'praktikum', 'kampus', 'tahun']
secondList = ['informatika', 'fungsional', 'UMM', '2020']

def zippedWords(firstWords, secondWords):
    words = []
    for (firstWord, secondWord) in zip(firstWords, secondWords):
        words.append(operator.add(firstWord, secondWord))
    return words

def convertWords(words, letterCase):
    return map(lambda word: defineLetterCase(word, letterCase), words)

def defineLetterCase(word, letterCase):
    if letterCase == 'lowercase':
        return word.lower()
    elif letterCase == 'uppercase':
        return word.upper()
    elif letterCase == 'capitalize':
        return word.capitalize()
    else:
        return word

zippedFirstList = zippedWords(firstList, secondList)
print(zippedFirstList)

zippedSecondList = zippedWords(firstList, secondList)
convertLetterSecondList = convertWords(zippedSecondList, 'lowercase')
print(list(convertLetterSecondList))

capitalizeFirstList = convertWords(firstList, 'capitalize')
capitalizeSecondList = convertWords(secondList, 'capitalize')
zippedThirdList = zippedWords(capitalizeFirstList, capitalizeSecondList)
print(tuple(zippedThirdList))

zippedFourthList = zippedWords(firstList, secondList)
convertLetterFourthList = convertWords(zippedFourthList, 'uppercase')
print(tuple(convertLetterFourthList))

#Robb - Mobile & Web Enthusiast

print('\n<<<Kegiatan 3>>>\n')

#Robb - Mobile & Web Enthusiast
