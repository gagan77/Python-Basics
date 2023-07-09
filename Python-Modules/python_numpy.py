import numpy as np

a = np.zeros(10) # 10 zeros
print(a) 

b = np.full((2,10),0.7) # 2x10 matrix of 0.7s
print(b)

c = np.linspace(0,25,7) # 7 numbers from 0 to 25
print(c)

print(type(c))