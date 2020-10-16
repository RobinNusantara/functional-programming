# Modul 1
# Kegiatan 1
numbers = []

length = int(input('Input panjang list : '))
print(f'\nPanjang list : {length}\n')

for index in range(0, length):
    element = int(input(f'Input element ke {index + 1} : '))
    numbers.append(element)

print(f'\nIsi List {numbers}')

#Robb

print('\n<<<Kegiatan 1>>>\n')

for number in numbers:  
    if number > 1:
        isPrime = True
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
        if isPrime:
            print(f'{number} termasuk bilangan Prima')
        elif number % 2 == 0:
            print(f'{number} termasuk bilangan Genap')
        else:
            print(f'{number} termasuk bilangan Ganjil')
    elif number == 1:
        print(f'{number} termasuk bilangan Ganjil')

#Kegiatan 2

print('\n<<<Kegiatan 2>>>\n')

def isPrimeNumber(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# def isEvenNumber(number):
#     return number % 2 == 0

isEvenNumber = lambda x: x % 2 == 0

for number in numbers:
    if number > 1:
        if isPrimeNumber(number):
            print(f'{number} termasuk bilangan Prima')
        elif isEvenNumber(number):
            print(f'{number} termasuk bilangan Genap')
        else:
            print(f'{number} termasuk bilangan Ganjil')
    elif number == 1:
        print(f'{number} termasuk bilangan Ganjil')

##Robb
