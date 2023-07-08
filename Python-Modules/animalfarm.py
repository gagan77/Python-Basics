#Example of namespacing and scoping

def d():
    animal = "Elephant"
    def e():
        nonlocal animal
        animal = "Cat"
        print("Inside nested functions:",animal)
        
    print("Before calling function:",animal)
    e()
    print("After calling function:",animal)
    
animal = "Dog"
d()
print("Global function:",animal)