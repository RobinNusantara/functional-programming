# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'e', 'g', 'h', 'i']

# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#   a  b  c  d  e <- stop right here at index -6
#   0  1  2  3  4  5  6  7  9  9
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

# 089613128351
# 085812257711
# 081237756640

# negative index
# -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
#  0   8   1   2   3   7   7   5   6   6   4   0  <- Phone Number
#  0   1   2   3   4   5   6   7   8   9  10  11
# index

phoneNumbers = []

length = int(input('Define how many phone numbers you want to input : '))

for index in range(length):
    element = input(f'Input {index} Phone Number : ')
    phoneNumbers.append(element)

def formatPhoneNumber(func):
    def phoneNumber(number):
        for index in number:
            func([f'+62 {index[-11:-5]} {index[-5:]}'])
    return phoneNumber

@formatPhoneNumber
def sortPhoneNumber(numbers):
    print(*sorted(numbers), sep="\n")

sortPhoneNumber(phoneNumbers)

#Robb Mobile & Web Enthusiast
