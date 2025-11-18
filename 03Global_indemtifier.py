#2. Global Identifier : declared outside of any functions and classes

# Example 1: 
#What if we have same local and global variable?

name = "John" #global variable
def display():
    name = "Doe" #local variable
    print("Inside function:", name)
    
display()
print("Outside function:", name)

print(100 * '-')
# Example 2:

age = 20
def global_func():
    print("Inside function: ", globals())
    
global_func()
print(100 * '-')
print("Outside function: ", globals())