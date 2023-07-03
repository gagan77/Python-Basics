#Control flow is the process of controlling the flow of a program.
#if statement is used to check a condition and execute a block of code if the condition is true.
#elif statement is used to check a condition and execute a block of code if the condition is true.
#else statement is used to execute a block of code if the condition is false.

#example 1
bill_total = 214

discount1 = 10
discount2 = 20

if bill_total >= 100:
    print("You have a 10 percent discount")
    bill_total = bill_total - discount1
elif bill_total >= 200:
    print("You have a 20 percent discount")
    bill_total = bill_total - discount2
else:
    print("You don't have a discount")
    
print("Your bill total is: $", bill_total)

#example 2
#Light is currently off
current = False

if current:
    current = False
    print('Turning light off')

if not current:
    current = True
    print('Turning light on')
    
#example 3
loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))

# Checkout more about condtional statements here: https://www.w3schools.com/python/python_conditions.asp