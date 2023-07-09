import pandas as pd

a = pd.DataFrame({"Animal": ["Dog", "Cat", "Horse","Elephant"], "Age": [2, 4, 7,6]})

print(a)
print(a.describe())

b = pd.DataFrame({
    "Letters": ["A", "B", "C", "D", "F"],
    "Numbers": [1, 2, 3, 4, 0] })

print(b.sort_values(by="Numbers"))

b = b.assign(new_values=b["Numbers"]*2)
print(b)