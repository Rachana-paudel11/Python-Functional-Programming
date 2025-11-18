# Positional vs Keyword Argumets
#Positional Arguments
'''
    1. The number of arguments must equals to no. of parameters
    2.. Must match the order of arguments and parameters
'''
def display(name, age):
    print(f"Name: {name}\nAge: {age}")
    
#display("John") # will throw error as it lacked one positional arguments
#display(20, "John") #won't match the order
display("John", 20)

#Keyword Argument
'''
    1. Order doesn't matter.
    2. No. of arguments must equals to no. of parameters
    
'''
def display_msg(name, msg):
    print(f"Message of the Day: {msg}\nWritten by: {name}")

display_msg( msg = "Smile", name = "Doe")

#Mixing positional and keyword argument
def output(name, age):
    print(f"\nName: {name}\nAge: {age}")
output("John", age = 27)