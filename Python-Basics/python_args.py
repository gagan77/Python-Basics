# Lets you pass in any number of args in the sum_of function
def sum_of(*args):
    sum = 0
    # to make sure it accounts for all the args we use the for loop
    for x in args:
        sum += x
    return sum

print(sum_of(1,2,6,45,23,1))