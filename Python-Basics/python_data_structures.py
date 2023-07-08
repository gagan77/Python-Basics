# Data structures are used to store and manipulate data efficiently.
# Python has three built-in data structures:

## List
print("########################LISTS###########################")
list1 = [1, 2, 3, 4, 5]

#To access 3 in list1
list1[2] # 2 is called the index of the list. It starts from 0.

list2 = ['a', 'b', 'c'] # list of strings
list3 = [1, 'a', 'abc', 2.0, True] # list of mixed data types
list4 = [1,[2,3,4],5] # list of lists

# to insert items in a list
list1.insert(len(list1),6) # insert 6 at index last position
list1.append(7) # insert 7 at index last position
list1.extend([8,9,10,11]) # insert 8 and 9 at index last position
print(list1)

#deleting items from a list
del list1[2] # delete the item at index 2
print(list1)

# to loop through a list
for i in list1:
    print(i)

## Tuple
print("########################TUPLES###########################")

# Tuples are similar to lists but are immutable.
my_tuple = (1,'strings',4.5,True,4.5)
print( my_tuple[2] ) # 4.5 is called the index of the tuple. It starts from 0.
print(type(my_tuple))
print(my_tuple.index(4.5)) # returns the index of 4.5 with the index where the value was found the first time
print(my_tuple.count(4.5)) # returns the number of times 4.5 is present in the tuple

# my_tuple[0] = 'new' # this will give an error as tuples are immutable

print("Tuple loop:")
for x in my_tuple:
    print(x)

print("########################SETS###########################")
## Sets - Don't allow any duplicates or have any order (Concept of Set theory)
set_a = {1,2,3,4,5,5}

set_a.remove(2) # removes 2 from the set
set_a.discard(3) # removes 3 from the set
set_a.pop() # removes the last item from the set
set_a.add(1)
set_a.add(2)
set_a.add(3)
print(set_a)

set_b = {4,5,6,7,8}
print(set_a.union(set_b)) # returns the union of the two sets
print(set_a |set_b ) # returns the union of the two sets

print(set_a.intersection(set_b)) # returns the intersection of the two sets
print(set_a & set_b) # returns the intersection of the two sets

print(set_a.difference(set_b)) # returns the difference of the two sets
print(set_a - set_b) # returns the difference of the two sets

print(set_a.symmetric_difference(set_b)) # returns the symmetric difference of the two sets
print(set_a ^ set_b) # returns the symmetric difference of the two sets

print("########################DICTIONARY###########################")
# Dictionary - It is a collection of key-value pairs.
sample_dict = {1: "Coffee", 2: "Green Tea", 3: "Milk Tea"}
print(sample_dict[1]) # returns the value of the key 1
sample_dict[2] = "Mint Tea" # updates the value of the key 2
del sample_dict[1] # deletes the key 1

print("Dictionary loop:")

for x in sample_dict:
    print(sample_dict[x])
