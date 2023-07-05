file1 = open("test.txt", mode="r")

data = file1.readline()
print(data)
file1.close()

# Use with open as it is better at exception handling and closing the file
with open("test.txt", mode="r") as file:
    data = file.read()
    print(data)