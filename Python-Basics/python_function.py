# Function in programming are modular pieces of code that can be reused.

# A function is defined by the keyword def followed by the function name,
# followed by a set of parentheses.

# The function body is indented to the next line and ends with a colon.
# The function body consists of statements that perform some action and return a value.
# The statements in a function body are executed sequentially.
# The variables passed in a function call are called function parameters.
def calculateTax(bill, tax_rate):
    return round((bill * tax_rate) / 100,2) # round(number, digits) => allows us to round the returned value as 2 decimal digits
    
# calculateTax(175,15) => 175 * 15 / 100 = 20.25
# The function call is made by using the function name followed by the set of parentheses.
print("Total tax is:", calculateTax(175,15))

# calculateTax(164.33,22) => 164.33 * 22 / 100 = 18.9
# The values passed in a function call are called function arguments.
print("Total tax is:", calculateTax(164.33,22))

# Checkout more about functions here: https://www.w3schools.com/python/python_functions