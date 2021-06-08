# Static and class methods #2

class person(object):
    population = 50
    
    # constructor method which initilizes name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # class method - call it on any instance of a class. we dont have to create an object to use this method. "person.getPopulation()" is an example of this working
    # all thats passed to a classmethod is the "cls" or whatever we want thats not "self". we can add as many parameters as we want. You can access static methods in your class method similiar to 
    # to the population we access
    @classmethod
    def getPopulation(cls):
        return cls.population

    # static method - similiar to class method but does not need a "self" or "cls" parameter. "person.isAdult(5)" - is the example. This is useful for organization. Used when you 
    # dont need self and dont need the actual object/class. Can be used for Math.methods(). Static method cant access the population however Class methods can access the methods in a class
    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')

newPerson = person('Tim', 18)

print(person.getPopulation())
print(person.isAdult(5))
print(newPerson.display())