# str[start:stop:stop]

# using the slice operator to reverse a string
str = "Hello World"
new_str = str[::-1]
print(new_str)

# using recursion to reverse a string
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
        
str = "reversal"
reverse = string_reverse(str)
print(reverse)