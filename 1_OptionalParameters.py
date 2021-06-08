# Optional parameters tutorial #1

#regular parameter
# def func(x):
#     return x **2

# call = func(5)
# print(call)

#optional parameters
def func(x=1):
    return x **2

# call = func(5)
# call2 = func()
# print("call: " + str(call))
# print("call2: " + str(call2))

def func2(word, freq=1):
    print(word*freq)

call = func2("chris")
call2 = func2("chris", 5)


#Method - functions taht belong to an object. A unique instance of a class. (i.e display, init below are methods of car class)

class car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
    
    def display(self, showAll=True):
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms." %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s." %(self.make, self.model, self.year))

whip = car('Ford', 'Fusion', 2012)
whip.display(False)