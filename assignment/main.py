import operator

_quadratic = lambda x: 2 * x ** 2 + 5 * x + 7

print(_quadratic(5))


length = int(input(f'Input length : '))

def _list(length):
    temp = []
    for index in range(length):
        element = input(f'Input element inside {index + 1} : ')
        temp.append(element)
    return temp

print('\n<<<Himpunan A>>>\n')
A = _list(length)
print('\n<<<Himpunan B>>>\n')
B = _list(length)

# Union/Gabungan
print('\n<<<Union>>>\n')

def _union(setA, setB):
    result = operator.add(setA, setB)
    return result

print(set(_union(A, B)))

# Intersection/Irisan
print('\n<<<Intersection>>>\n')

def _intersection(setA, setB):
    result = set(filter(lambda val: val in setB, setA))
    return result

print(_intersection(A, B))

# Difference/Selisih
print('\n<<<Difference>>>\n')

def _difference(setA, setB):
    result = set(filter(lambda val: val not in setB, setA))
    return result

print(_difference(A, B))

# Symmetric Difference
print('\n<<<Symmetric Difference>>>\n')

def _symmetricDiff(setA, setB):
    return set(setA).symmetric_difference(set(setB))

print(_symmetricDiff(A, B))

#Robin Nusantara - 201810370311174
