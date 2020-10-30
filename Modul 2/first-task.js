console.log('\n<<<Kegiatan 1>>>\n');

const words = ['I', '❤️', 'PYTHON', 'AND', 'JAVASCRIPT'];

console.log('<<<MAP>>>\n');
function iterateWords(wordList) {
    const newWordList = [];
    for (const word of wordList) {
        newWordList.push(word);
    }
    return newWordList;
}

console.log('With Pure Function');
console.log(iterateWords(words));

console.log('With Map Function');
console.log(words.map((word) => word));

console.log('\n<<<Filter>>>\n')
function filterWords(wordList) {
    const newWordList = [];
    for (const word of wordList) {
        if (word.includes('A')) {
            newWordList.push(word);
        }
    }
    return newWordList;
}

console.log('With Pure Function');
console.log(filterWords(words));

console.log('With Filter Function');
console.log(words.filter((word) => word.includes('A')));

//Robb - Mobile & Web Enthusiast
