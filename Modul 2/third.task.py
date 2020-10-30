print('\n<<<Kegiatan 3>>>\n')

numbers = ((1, 2), (3, 4))

def square(listNumber):
    newListNumber = []
    for i in listNumber:
        for j in i:
            newListNumber.append(pow(j, 2))
    return tuple(newListNumber)

print(square(numbers))

#Robb - Mobile & Web Enthusiast
