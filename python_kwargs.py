# kwargs = keyword arguments
# takes in keyword arguments and the non-keyword variables
def sum_of(**kwargs):
    sum = 0
    for k,v in kwargs.items(): 
        sum += v # sum += v.value
        print(k,v) # print key and value
    return round(sum,2) # round to 2 decimal places

print(sum_of(coffee=2.99,cake=4.55,juice=2.99))