# import modules
from random import randint # import method for random int

# if controller test
'''
x = 0
if x:
    print x
    print 'cool'
else:
    print (not x) - 1
    print 'not cool'
print 'fine'

y = 10
if y == 0:
    print "zero"
else:
    if True:
        print 1
    print "not zero"
'''
# while controller test
'''
counter = 0
while counter < 10:
    print counter
    counter += 1
    # counter++     # this is not valid
    if(counter == 5):
        break
'''
# guess number game

num = randint(1, 100)
correct = False
print 'Guess what I think?'

while not correct:
    answer = int(input())
    if answer < num:
        print 'Too small!'
    if answer > num:
        print 'Too large!'
    if answer == num:
        correct = True
        print 'BINGO!'
