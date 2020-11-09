import operator
import functools

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

for product in products:
    print(product)

print('\n<<<Kegiatan 1.1>>>')

print('\n<<<Kegiatan 1.2>>>\n')
products.pop(1)
for product in products:
    print(product)

print('\n<<<Kegiatan 1.3>>>\n')


for product in products:
    print('Product Name    : ', product.get("productName"))
    print('Product Amount  : ', product.get("productAmount"))
    print('---------')

print('\n<<<Kegiatan 1.4>>>\n')
products.append({
    'productName': 'Speaker',
    'productAmount': 7000,
    'productQuality': 'Standard',
    'productPrice': 600
})

for product in products:
    print(product)

print('\n<<<Kegiatan 1.5>>>\n')
for product in products:
    increasePrice = operator.add(product.get('productPrice'), 500)
    product.update({'productPrice': increasePrice})

for product in products:
    print(product)

print('\n<<<Kegiatan 1.6>>>\n')
for product in products:
    print('Product Name    : ', product.get("productName"))
    print('Product Amount  : ', product.get("productAmount"))
    print('---------')

print('\n<<<Kegiatan 1.7>>>\n')
products[3].update({'productQuality': 'Second'})
products[0].update({'productAmount': 125})
products[1].update({'productPrice': 1230})

for product in products:
    print(product)

print('\n<<<Kegiatan 1.8>>>\n')
for product in products:
    print('Product Name    : ', product.get("productName"))
    print('Product Amount  : ', product.get("productAmount"))
    print('---------')

print('\n<<<Kegiatan 1.9>>>\n')

totalAmount = functools.reduce(lambda acc, val: acc + val.get('productAmount'), products, 0)
print(f'Total Amount : {totalAmount}')
totalPrice = functools.reduce(lambda acc, val: acc + val.get('productPrice'), products, 0)
print(f'Total Price  : {totalPrice}')

print('\n<<<Kegiatan 1.10>>>\n')

mergeKey = lambda product: operator.add(product.get('productName'), product.get('productQuality'))
print(list(map(mergeKey, products)))

#Robb Mobile & Web Enthusiast
