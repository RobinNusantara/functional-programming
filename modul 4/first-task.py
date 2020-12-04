# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'e', 'g', 'h', 'i']

# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#   a  b  c  d  e <- stop right here at index -6
#   0  1  2  3  4  5  6  7  8  9
#  start from 0
# print(alphabet[-10:-5])
# equivalent
# print(alphabet[0:5])

#       -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#     start from here -> e  f  g  h  i 
#         0  1  2  3  4  5  6  7  8  9
# print(alphabet[-5:])
# equivalent
# print(alphabet[5:])

# 085812257711
# 089613128351
# 081237756640

# negative index
# -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
#  0   8   1   2   3   7   7   5   6   6   4   0  <- Phone Number
#  0   1   2   3   4   5   6   7   8   9  10  11
# index

phoneNumbers = []

length = int(input('Define how many phone numbers you want to input : '))

for index in range(length):
    element = input(f'Input phone number - {index + 1}: ')
    phoneNumbers.append(element)

def formatPhoneNumber(func):
    def phoneNumber(numbers):
        _slice = lambda elm: f'+62 {elm[slice(-11, -5)]} {elm[slice(-5, None)]}'
        func(map(_slice, numbers))
    return phoneNumber

def sortPhoneNumber(func):
    def phoneNumber(numbers):
        func(sorted(numbers))
    return phoneNumber

@sortPhoneNumber
@formatPhoneNumber
def sortedList(numbers):
    print(*numbers, sep='\n')

@formatPhoneNumber
def unsortedList(numbers):
    print(*numbers, sep='\n')

print('\n<<<Sorted List>>>\n')
sortedList(phoneNumbers)

print('\n<<<Unsorted List>>>\n')
unsortedList(phoneNumbers)

#Robb Mobile & Web Enthusiast
