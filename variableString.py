# string type test
'''
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
'''
#print '''***Conversation***
#"What's your name?" I asked.
#"I'm Spencer"
#***Conversation End***'''
'''
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
'''
# template string
num = 18
print 'My age is %d' % num
print 'Price is %f' % 4.99      # result is 4.990000
print 'Price is %.2f' % 4.99    # result is 4.99
print 'Price is %.3f' % 4.9995  # result is 5.000
name = "Spencer"
print '%s is a good guy.' % name
#print 'I have been studying %s for %d years.' % 'game design' 2 
print 'I have been studying %s for %d years.' % ('game design', 2) # ('game design', 2) is a tuple data

# format template functions
s = '{name} has {num} messages.'
print s.format(name = 'Spen', num = 30)
#print s.format_map(vars()) # formap_map is a python3 function
