# global scope accessible in all scope
my_global = 10

def fn1():
    enclosed_var = 8 # accessible in enclosed and local scope
    def fn2():
        local_var = 20 # accessible in local scope only
        print("Access to Global variable",my_global)
        print("Access to Enclosed variable",enclosed_var)
    
    fn2()
fn1()

print(enclosed_var)
print(local_var)