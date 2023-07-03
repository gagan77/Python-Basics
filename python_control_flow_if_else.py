#Control flow is the process of controlling the flow of a program.
#if statement is used to check a condition and execute a block of code if the condition is true.
#elif statement is used to check a condition and execute a block of code if the condition is true.
#else statement is used to execute a block of code if the condition is false.

bill_total = 114
discount1 = 10


if bill_total >= 100:
    print("You have a 10 percent discount")
    bill_total = bill_total - discount1
else:
    print("You don't have a discount")
    
print("Your bill total is: $", bill_total)
