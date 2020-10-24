import operator

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

zippedDict = zip(firstList, secondList)
print(dict(zippedDict))

#Robb - Mobile & Web Enthusiast
