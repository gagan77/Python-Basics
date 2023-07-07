# Object Oriented Programming (1 of many Paradigms)
# relies on simplicity and flexibility to reduce workflow
# High modularity which makes it easier to maintain and extend the code

# Classes
# Classes are blueprints for objects (contains Attributes and Behaviors)

# Encapsulation
# The idea of encapsulation is to have methods and variables within the bounds of a given unit.
# Encapsulation is also used for hiding data and its internal representation. 
class Alpha:
    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 2.  # Private member ‘b’
        
# Polymorphism
# Polymorphism refers to something that can have many forms. In this case, a given object. 
# Remember that everything in Python is inherently an object, so when I talk about polymorphism, it can be an operator, 
# method or any object of some class.

# Inheritance
# class Parent:
#     Members of the parent class

# class Child(Parent):
#     Inherited members from parent class
#     Additional members of the child class

# Abstraction
# Abstraction can be seen both as a means for hiding important information as well 
# as unnecessary information in a block of code. The core of abstraction in Python is the 
# implementation of something called abstract classes and methods, which can be implemented by 
# inheriting from something called the abc module. 
