#closure

firstValue = int(input('Input First Value : '))
secondValue = int(input('Input Second Value : '))

def closureMultiplier(y):
    def multiply(x):
        return x * y
    return multiply

result = closureMultiplier(firstValue)(secondValue)
print(f'Result : {result}')

#decorator

def decoratorMultipiler(func):
    def multiply(firstValue, secondValue):
        return func(firstValue, secondValue)
    return multiply

@decoratorMultipiler
def multiplyDecorator(firstValue, secondValue):
    print(f'Result : {firstValue * secondValue}')

multiplyDecorator(firstValue, secondValue)
