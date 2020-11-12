import sys
import operator
import functools
import pprint
sys.path.insert(1, '/Users/robin/VisualStudioCodeProjects/functional-programming/utils')
from utils import printDictInsideList

# Kegiatan 1
print('\n<<<Original Dictionary>>>\n')

products = [
    {
        'productName': 'Computer',
        'productAmount': 50,
        'productQuality': 'New',
        'productPrice': 5000000
    },
    {
        'productName': 'Keyboard',
        'productAmount': 3000,
        'productQuality': 'Standard',
        'productPrice': 200000
    },
    {
        'productName': 'Mouse',
        'productAmount': 2500,
        'productQuality': 'Standard',
        'productPrice': 70000
    },
    {
        'productName': 'Transformator',
        'productAmount': 120,
        'productQuality': 'New',
        'productPrice': 600000
    },
    {
        'productName': 'Cable',
        'productAmount': 15000,
        'productQuality': 'Standard',
        'productPrice': 2500
    },
]

pprint.pprint(products)

print('\n<<<Kegiatan 1.1>>>')

def filterDict(dictionary, selectedKey):
    temp = {}
    for key in dictionary:
        if key in selectedKey:
            temp.update({key: dictionary.get(key)})
    return temp

pprint.pprint(list(map(lambda product: filterDict(product, ['productAmount', 'productPrice']), products)))

print('\n<<<Kegiatan 1.2>>>\n')
products.pop(1)
pprint.pprint(products)

print('\n<<<Kegiatan 1.3>>>\n')

printDictInsideList(products)

print('\n<<<Kegiatan 1.4>>>\n')
products.append({
    'productName': 'Speaker',
    'productAmount': 7000,
    'productQuality': 'Standard',
    'productPrice': 600
})

pprint.pprint(products)

print('\n<<<Kegiatan 1.5>>>\n')
for product in products:
    updatePrice = operator.add(product.get('productPrice'), 500)
    product.update({'productPrice': updatePrice})

pprint.pprint(products)

print('\n<<<Kegiatan 1.6>>>\n')

printDictInsideList(products)

print('\n<<<Kegiatan 1.7>>>\n')
products[3].update({'productQuality': 'Second'})
products[0].update({'productAmount': 125})
products[1].update({'productPrice': 1230})

pprint.pprint(products)

print('\n<<<Kegiatan 1.8>>>\n')
printDictInsideList(products)

print('\n<<<Kegiatan 1.9>>>\n')

def countTotal(key, itemList):
    return functools.reduce(lambda acc, val:  acc + val.get(key), itemList, 0)

print(f'Total Amount : {countTotal("productAmount", products)}')
print(f'Total Price  : {countTotal("productPrice", products)}')

print('\n<<<Kegiatan 1.10>>>\n')

mergeKey = lambda product: operator.add(product.get('productName'), product.get('productQuality'))
print(list(map(mergeKey, products)))

#Robb Mobile & Web Enthusiast
