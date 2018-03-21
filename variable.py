# variable test
'''
name = "Spencer"
myVar = 123
price = 5.99
visible = True
print name
'''
# string type test

print 'good'
_str = 'bad'
print _str
# print str + 1     # this is not valid
print 'not ' + _str
print "It's good"
print 'not "Bad"'
print "I\'m\0\"Good\"\nHow about you\\him"
print "I will not \
change line"
print ()
print ('')
print '''***Conversation***
"What's your name?" I asked.
"I'm Spencer"
***Conversation End***'''
print ''
print "He said",
print "he was the chosen one."

print not 'str'   # result is false
print 'str' or 1  # result is str

num = "123"
print int(num) + 5
print float(num) + 2.2
print str(int(num) + 10) + num
num = "321.23"
# print int(num)    # this is not valid
print float(num) + 3.3
print str(float(num) + 11.4) + num
print (float(num) + 1).__str__()
print False.__str__()
print num.__str__()

# change variable type
'''
a = 123
print a
a = 'hi'
print a
'''
# apply calculation to the right side
'''
value = 3 * 4
print value
value = 2 < 5
print value
'''
# use input on variables
'''
name = input()
print name
'''