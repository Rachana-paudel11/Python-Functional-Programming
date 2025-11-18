#Return statement - returns the value to the function call and stop execution
def area(l, b):
    area_of_rect = l * b
    return area_of_rect

#global variables
length  = 10
breadth = 5

rectangle  = area(length, breadth) #holds the return value
print(f"Area of Rectangle: {rectangle}\n")

#1. Can return any type of python object
def display():
    return 'Rachana'

print(display())

#2. Can return multiple values
def calc(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul

addition, subraction , multiplication = calc(12, 3)
print(f"\nAddition: {addition}\nSubraction: {subraction}\nMultiplication: {multiplication}")

#3. Return statement must be last statement of function
def msg():
    return "\nHi there"
    print("This won't be execute")

var = msg()
print(var)

#4. Default return type is none
def default():
    y =  1
    
print(default()) #no return value so it returns none