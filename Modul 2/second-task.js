const firstList = ['jurusan', 'praktikum', 'kampus', 'tahun'];
const secondList = ['informatika', 'fungsional', 'UMM', '2020'];

function combineElement(firstList, secondList) {
    const newList = [];
    for (let firstItem = 0; firstItem < firstList.length; firstItem++) {
        for (let secondItem = 0; secondItem < secondList.length; secondItem++) {
            if (firstItem === secondItem) {
                newList.push(firstList[firstItem] + secondList[secondItem])
            }
        }
    }
    return newList
}

function convertLetterCase(wordList, letterCase) {
    return wordList.map((wordItem) => defineLetterCase(wordItem, letterCase));
}

function defineLetterCase(wordItem, letterCase) {
    if (letterCase === 'uppercase') {
        return wordItem.toUpperCase();
    } else if (letterCase === 'lowercase') {
        return wordItem.toLowerCase();
    } else {
        return wordItem;
    }
}

console.log(combineElement(firstList, secondList))
