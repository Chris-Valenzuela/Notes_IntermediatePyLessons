# Map Function #3

# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.) 
# map(fun, iter)

li = [1,2,3,4,5,6,7,8,10]

def func(x):
    return x**x

# Lets apply the function x to every value in the li list

newList = []
for x in li:
    newList.append(func(x))
print(newList)

# This is essentially a short cut. Each iterator in the list gets the function applied to it and then returned as a function 
print(list(map(func, li)))

# This is doing it in a list comprehension [] returns it to a list. Adding the modulo is a condition only for even numbers
print([func(x) for x in li if x % 2 == 0])