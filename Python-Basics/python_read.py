# read - returns the entire content of the file as a string
with open('test.txt', 'r') as file:
    print(file.read()) # prints the entire content of the file
    
# #readline - returns a list of strings, each representing a line of the file
with open('test.txt', 'r') as file:
    print(file.readline()) # prints the first line of the file
    
# #readline() - reads the entire contents of the file and returns it in an ordered list
with open('test.txt', 'r') as file:
    print(file.readlines()) # prints the entire file in a list of strings
    
with open("test.txt", "r") as file:
    for line in file:
        print(line)