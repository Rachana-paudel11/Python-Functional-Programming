#Scope : Region where specified variables and identifier can be accessed

# Variable VS Identifier
'''
    Identifier: name given to any object which can be variables, function name , class name 
    
    Variable: specific type of identifier given to any value which is also a memory 
    location to store a value
'''
 
#Local Identifier: identifier defined inside the fuction
# scope of local identifier and variables: inside the fuction definition
def greeting(name):
    message = "Hi"
    print(f"{message}, {name}")

greeting("Rachana")

#Garbage collector : after function execution all the variables or identifiers is removed from the RAM

#locals(): return dictionary or key-value paired inside a function
def display(name):
    age = 22
    x = locals()
    print(f"{name} is {age} years old.")
    
    print(f"locals(): {x}")
    print(f"lenght of local(): {len(x)}")
    print(x['age']) #as locals() returns key-value paired
display("Ridam")
