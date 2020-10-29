import emoji

print('\n<<<Kegiatan 1>>>\n')

redHeart = emoji.emojize(':red_heart:', variant='emoji_type')

words = ['I', redHeart, 'PYTHON', 'AND', 'JAVASCRIPT']

print('<<<Map>>>\n')
def iterateWords(wordList):
    newListWord = []
    for word in wordList:
        newListWord.append(word)
    return newListWord

print('With Pure Function')
print(iterateWords(words))

print('With Map Function')
print(list(map(lambda word: word, words)))

print('\n<<<Filter>>>\n')
def filterWords(wordList):
    newListWord = []
    for word in wordList:
        if 'A' in word:
            newListWord.append(word)
    return newListWord

print('With Pure Function')
print(filterWords(words))

print('With Filter Function')
print(list(filter(lambda word: 'A' in  word, words)))

#Robb - Mobile & Web Enthusiast
