class Recipe():
    def __init__(self,dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        print("The " + self.dish + " recipe consists of: " + \
              str(self.items) + " and takes" + str(self.time)  + " min to prepare")
        
pizza = Recipe("Pizza", ["cheese", "tomato", "pepperoni"], 20)
cake = Recipe("Cake", ["flour", "sugar", "eggs"], 10)

print(pizza.items)
print(cake.items)

print(pizza.contents())