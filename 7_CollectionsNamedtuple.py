# Collections Named Tuple #7

import collections
from collections import namedtuple

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

# Named tuples assign meaning to each position in a tuple and allow for more readable self documenting code. They can be used wherever regular tuples are used and they
# have the ability to acces fields by name instead of position index 

#so this x y z automatically breaks it up into three different paramenters. You could use a list or any iterable object
point = namedtuple('Point', 'x y z')

newP = point(3,4,5)
print(newP)

pointB = namedtuple('Point', {'x':0, 'y':0, 'z':0})
newPb = pointB(1,2,3)

#so now we can accees each element by name (which we can do on a regular tuple)
print(newPb.x)
# can also acess as a if it were a normal tuple
print(newPb[0])

print(newP._fields)

newvale = newPb._replace(y=6)
print(newvale)

make = point._make(['a', 'b', 'c'])
print(make)