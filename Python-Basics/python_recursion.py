# Factorial - using recursion
# the bad is it uses too much memory
# the good is it is easy to read and understand
def factorial(n):
    if n == 0: # base case
        return 1
    else: # inductive step
        return n * factorial(n-1)
    
print(factorial(5))