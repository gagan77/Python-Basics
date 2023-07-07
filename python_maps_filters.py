menu = ["espresso", "latte", "cappuccino","cortado","americano"]

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee

#map passes the function to each element of the list
#menu the list which you would like to pass to the function
map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)

# only the 
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)
    
# Maps take all objects in a listand applies a function to each of them
# Filters take all objects in a list and applies a function to each of them

z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)