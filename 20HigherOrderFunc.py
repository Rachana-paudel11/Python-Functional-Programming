#Condition for Higher Order Function
'''
    1. Takes another function as a argument
    2. returns function as an output
'''
#function as argument
def addition(a1, a2):
    return a1+a2
def display(func):
    func(10, 20)
display(addition)
    
#returns function as a output
def greet():
    print("Inside Greet function")
    
    def mini_greet():
        print("Hi")
    return mini_greet
d = greet()
d()