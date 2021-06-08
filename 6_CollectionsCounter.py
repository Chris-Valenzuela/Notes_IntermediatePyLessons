# Collections #6

import collections
from collections import Counter

# collections is a built module in python which allows us to hav edifferent types of datatypes

#Containers - datatype that stores multiple objects 4 main containers in Python:
    # list
    # set 
    # dict
    # tuple - immutable

# 5 Types of collections :
    #1 counter
    #2 deque
    #3 namedTuple()
    #4 orderdDict
    #5 defaultDict

# can take in any container/datatype. They are their own types
c = Counter('chris')
# print(type(c))
print(c)
b = Counter(['a', 'a', 'b', 'c'])
print(b)
e = Counter({'a':1, 'b':2})
print(e)
f = Counter(cats=2, dogs=7, sharks =4)
print(f)
print(f['cats'])
# whats cool is this doesnt give us an error BUT a dictionary would.
print(f['pet'])

# this prints out a made list with the amount of indices mentioned
print(list(b.elements()))
print(list(f.elements()))

# returns us the most common in a tuple fashio
print(c.most_common(2))
print(f.most_common(2))

g = Counter(a=4, b=2, c=0, d=-2)
g.subtract(b)
print(g)
g.update(b) # this is pretty much adding 
print(g)

# g.clear()
# print(g)

print(c+g)
print(c-g)
print(c & g) #intersection takes the minmum shown of all those elements 
print(c | g) #union takes the max of each key

# Collections Coutner Python Documentation 