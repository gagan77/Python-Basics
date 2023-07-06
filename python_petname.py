import random

f = open("petnames.txt", "r") #open file
f_content = f.read() #read file content
f_content_list = f_content.split("\n") #split file content into list
print("The random chosen pet name is:")
print(random.choice(f_content_list))

