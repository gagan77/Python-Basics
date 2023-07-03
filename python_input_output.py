#Every application will reqiure data to come into it or be passed in by used.
#This is where input comes in.
#It is a function that allows you to take in data from the user.

#The following code asks the user for two numbers and adds them together.
num1 = int(input("Please enter a first number: "))
num2 = int(input("Please enter a second number: "))

#prints the type of the variable num1, if one is a float and one int then float will be the result
#always use type to makesure you are getting the right type of data
print(type(num1))

#prints the summation of the two numbers
print(num1 + num2)

# Check out more about this on
# https://www.w3schools.com/python/ref_func_type.asp