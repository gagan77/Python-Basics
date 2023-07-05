# try and catch is used to handle exceptions

# Excercises

# index error
try:
    items = [1,2,3,4,5]
    item = items[6]
    print(item)
except IndexError as e:
    print(e)
    
    
#ZeroDivisionError
def divide_by(a,b):
    return a/b

try:
    ans = divide_by(50,0)
except ZeroDivisionError as e: #specific exception
    print(e, "we cannot divide by zero")
except Exception as e: #general exception
    print(e, "Catches them all")
    
#FileNotFoundError
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")  