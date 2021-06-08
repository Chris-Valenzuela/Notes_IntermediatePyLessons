# Lambda function #5

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

def func(x):
    return x + 5

# sometimes u dont want to write simple functions out. 

# lambda is used only if u have 1 expressions and fits on one line
func2 = lambda x: x + 5

print(func2(1))
print(func2(4))


# using a lambda inside a function (function within a function) but you dont want to create a new one. u can just create it like so
def func3(x):
    func2 = lambda x: x + 5
    return func2(x) + 50

print(func3(1))

# you could do everything like a normal function even optional parameters. But you can only use one expression 
func4 = lambda x,y=4: x+y
print(func4(1))


a = [1,2,3,4,5,6,7,8,9,10]

#instead of create a new function right above we jsut use lambda
newlist = list(map(lambda x: x+5, a))
print(newlist)
newlist2 = list(filter(lambda x: x%2==0, a))
print(newlist2)