# import modules
from random import randint

# function test
'''
def SayHello():
    print 'Hello world!'

SayHello()
# function with arguments
def SayHelloToSomeone(someone):
    s = '{name} says hello'
    print s.format(name = someone)

SayHelloToSomeone('Spencer')

def Exponentiation(base, index):
    if base or index > 0:
        value = 1.0
        if index > 0:
            for i in range(0, index):
                value *= base
        if index < 0:
            for i in range(index, 0):
                value /= base
        print value
        return True
    else:
        print 'Base number should not be 0 when index <= 0'
        return False

Exponentiation(0, -1)
Exponentiation(0, 2)
Exponentiation(-5, 0)
Exponentiation(5, 4)
Exponentiation(4, -3)
'''
# Guess number game

def IsEqual(num1, num2):
    if num1 < num2:
        print 'Too small'
        return False
    if num1 > num2:
        print 'Too large'
        return False
    if num1 == num2:
        print 'Correct'
        return True

num = randint(1, 100)
print 'Guess the number between 1 and 100'
correct = False
while not correct:
    answer = input()
    correct = IsEqual(answer, num)

    
