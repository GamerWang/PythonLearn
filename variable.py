# variable test
'''
name = "Spencer"
myVar = 123
price = 5.99
visible = True
print name
'''
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
# variable convertions
# int(x)
# float(x)
# str(x)
# bool(x)
print bool('False') # result is True
print bool('')      # result is False
# these variables are considered False when convert to bool
# 0 value numbers: 0, 0.0
# empty string: '', ""
# null value: None
# empty set: (), [], {}
# all other values are true
# when variable show in condition, it will automatically call bool conversion
a = ''
if a:
    print "String not empty."
else:
    print "String empty."