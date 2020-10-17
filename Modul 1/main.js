numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

console.log('\n<<Kegiatan 1>>\n')

for (number of numbers) {
    if (number == 1) {
        console.log(`${number} termasuk bilangan Ganjil`)
    } else {
        let isPrime = true
        for (i = 2; i < number; i++) {
            if (number % i == 0) {
                isPrime = false
            }
        }
        if (isPrime) {
            console.log(`${number} termasuk bilangan Prima`)
        } else if (number % 2 == 0) {
            console.log(`${number} termasuk bilangan Genap`)
        } else {
            console.log(`${number} termasuk bilangan Ganjil`)
        }
    }
}

console.log('\n<<Kegiatan 2>>\n')

function isPrimeNumber (number) {
    for (i = 2; i < number; i++) {
        if (number % i == 0) return
    }
    return true
}

const isEvenNumber = (number) => number % 2 == 0

numbers.map(function(number) {
    if (number == 1) {
        console.log(`${number} termasuk bilangan Ganjil`)
    } else {
        if (isPrimeNumber(number)) {
            console.log(`${number} termasuk bilangan Prima`)
        } else if (isEvenNumber(number)) {
            console.log(`${number} termasuk bilangan Genap`)
        } else {
            console.log(`${number} termasuk bilangan Ganjil`)
        }
    }
})
