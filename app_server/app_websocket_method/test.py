from collections import Counter

list = ['a','b','c','a','d','b']
v = Counter(list)
print v
v = Counter(list).most_common(2)
print v
print v[0]
print v[0][1]
print v[1][1]
if v[1][1] == v[0][1]:
    print 'here'