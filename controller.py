# import modules
from random import randint # import method for random int

# if controller test

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

a = randint(1, 3)
if a == 1:
    print 'one'
elif a == 2:
    print 'two'
elif a == 3:
    print 'three'
else:
    print 'much'

# while controller test
'''
counter = 0
while counter < 10:
    counter += 1
    if counter == 2:
        continue
    print counter
    # counter++     # this is not valid
    if (counter == 5):
        break
'''
# for controller test
'''
for i in range(1, 101):
    print i # print 1 to 100

for i in range(0, 10):
    if i == 1:
        continue
    print i
    if i == 5:
        break
'''
# guess number game
'''
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
'''