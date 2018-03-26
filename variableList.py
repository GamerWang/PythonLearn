# variable type test
l = range(1, 10)
for i in l:
    print i

l = [3, 1, 4, 1, 5, 9]
print l[0]

l = [365, 'everyday', 0.618, True]
l[0] = 24
#l[4] = False   # this is not valid
l.append(False)
del l[2]
for i in l:
    print i