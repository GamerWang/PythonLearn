'''
# basic operations
# a > b
# a < b
# a >= b
# a <= b
# a == b
# a != b
# not a
# a and b
# a or b
'''
'''
# operation and value tests
a = 1 < 3
print a
b = 1
c = 3
print b > c
print b == c
print b != c
print a != b
print a == b
b = 2
print a == b
print False == 0
d = False + 1
print d
print not d
print 1 and 2
print 0 and 1
print False or 1
print 1 or False
print False and 1
print 1 and False
print 1 or (1 + 1 and 3)
'''
# guess number game
num = 10
print 'Guess what I think?'
answer = int(input())

result = answer < num
print 'too small?',
print result

result = answer > num
print 'too large?',
print result

result = answer == num
print 'equal?',
print result