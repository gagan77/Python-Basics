f1 = open("test.txt","r")
first_line = f1.readline()

print(first_line)

f2 = open("output.txt","w")
f2.write(first_line)

f1.close()
