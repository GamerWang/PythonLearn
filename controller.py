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

# guess number game
'''
num = 10
print 'Guess what I think?'
answer = int(input())
if answer < num:
    print 'Too small!'
if answer > num:
    print 'Too large!'
if answer == num:
    print 'BINGO!'
'''