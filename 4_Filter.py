# Filter Function #4

# Filter and map are usually used together. The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
# filter(function, iterable) - takes in the same arguements as map 

def add7(x):
    return x+7

def isOdd(x):
    return x % 2 != 0 

a = [1,2,3,4,5,6,7,8,9,10]

# this is useful because we can do this instead of running a for loop with conditions 
b = list(filter(isOdd, a))
print(b)

# here we are adding 7 to each filterd list
c = list(map(add7, filter(isOdd, a)))
print(c)

# Use Case: We can use filter to return things that have a certain digit or string etc.. 