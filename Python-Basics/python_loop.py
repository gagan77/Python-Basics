#In programming loop is used to repeat a block of code for a given number of times.
#While loop is used to repeat a block of code while a given condition is true.
#For loop is used to repeat a block of code for a given number of times.

str = "Hello World"
# i represents the index of the string
# in programming the index starts from 0
# in this case while there are 11 characters in the string the last character is at position 10
for i in str:
    print(i)
    
hobbies = ["code","read","workout","sleep", "watch movies"]

#for loop is used to iterate over a list EASIER
for idx, item in enumerate(hobbies):
    print(idx, item)
    
#while loop is used to iterate over a list MORE Involved process
count = 0
while count < len(hobbies):
    print("I like to " + hobbies[count])
    count += 1
    
#Another example of for loop and why its easier
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    print('One of my favorite desserts is', dessert)
    
# Example with conditional within a for loop
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert)
        break # used to stop the loop when the condition is met
else:
    print('No sorry, that dessert is not on my list')
    

# Nested Loops
for i in range(10):
    for j in range(10):
        print(i,j,end=" ")
    print()