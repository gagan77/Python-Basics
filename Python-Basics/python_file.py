with open("test.txt", mode="a") as file: #opens the file or makes a new file in write mode and assigns it to the variable "file"
    file.writelines(["Hello World", "\nThis is another line", "\nThis is the last line"]) #writes to the file

# Replaces the current file - if we choose the mode as w or r+
# the mode of a will append to the existing file
