# Nested Function
def outer():
    print("I am global function!")
    def inside(): #local function
        print("I am inside the function.")
    inside() #can only be accessed in the local scope
outer() # can be accessed globally