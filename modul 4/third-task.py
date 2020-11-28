#closure

firstValue = input('Input First Value : ')
secondValue = input('Input Second Value : ')

def closureMultiplier(y):
    def multiply(x):
        return x * y
    return multiply

multiplyClosure = closureMultiplier(int(firstValue))
result = multiplyClosure(int(secondValue))
print(f'Result : {result}')

#decorator

def decoratorMultipiler(func):
    def multiply(firstValue, secondValue):
        return func(firstValue, secondValue)
    return multiply

@decoratorMultipiler
def multiplyDecorator(firstValue, secondValue):
    print(firstValue * secondValue)

multiplyDecorator(int(firstValue), int(secondValue))
