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

print(zippedWords(firstList, secondList))

zippedSecondList = zippedWords(firstList, secondList)
print(list(convertWords(zippedSecondList, 'lowercase')))

converFirstList = convertWords(firstList, 'capitalize')
convertSecondList = convertWords(secondList, 'capitalize')
print(tuple(zippedWords(converFirstList, convertSecondList)))

zippedFourthList = zippedWords(firstList, secondList)
print(tuple(convertWords(zippedFourthList, 'uppercase')))

zippedDict = zip(firstList, secondList)
print(dict(zippedDict))

#Robb - Mobile & Web Enthusiast
