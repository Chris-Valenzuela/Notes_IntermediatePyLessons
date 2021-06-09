# Collections Deque #8

import collections
from collections import deque

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

# a deque looks similiar to a list. But it is faster to add elements to the end or beginning of the list. But for random areas its better to use a list. 

d = deque("hello")

print(d)

d.append(4)
d.appendleft('5')
print(d)

d.pop()
# removes the first elemnt instead of the last
d.popleft()
print(d)

d.clear()
print(d)

# this is a good use case for not having to use a for looop to add stuff
# extend takes an iterable argument and puts it to the end of  the list
d.extend('456')
print(d)
d.extend([1,2,3])
print(d)
#note this is added in reverse order
d.extendleft('hey')
print(d)

# -1 rotates to the left and +1 rotates to the right by the integer position
d.rotate(-1)
print(d)
d.rotate(2)
print(d)

# maxlen removes the first/last element (depending on append or appendleft method) from the deque in order to append
e = deque('hello', maxlen=5)
print(e)
e.appendleft(1)
print(e)