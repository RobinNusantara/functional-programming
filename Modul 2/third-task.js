console.log('\n<<<Kegiatan 3>>>\n');

const numbers = [[1, 2], [3, 4]];

function square(listNumber) {
    const newListNumber = [];
    for (const i of listNumber) {
        for (const j of i) {
            newListNumber.push(Math.pow(j, 2));
        }
    }
    return newListNumber;
}

console.log(square(numbers));

