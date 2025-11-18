#Normal Function
def add(a, b):
    return a + b 
print(f"Normal  Function: {add(2, 3)}")

#Lambda function 
addition = lambda x , y : x + y 
print(f"Lambda Function: {addition(2, 3)}")

#Lamba function returns only one value 
'''
calc = lambda u , v : u + v , u - v # Lambda has only one expression as well
'''
# to get rid of this we use Collection
calc = lambda u , v : (u + v , u - v) # returns tuple 

# print(f"{calc(10, 20)}")

addition, subraction = calc(10 , 20)
print(f"\nAddition: {addition}")
print(f"Subraction: {subraction}")

#increment number 
incre = lambda n : n+ 1
print(f"Increment: {incre(3)}")

#square of number 
square = lambda m : m**2
print(f"Square: {square(19)}")

#To upper
uppercase = lambda word: word.upper()
print(f"Upper: {uppercase('Rachana')}")

#Fahrenheit
fahrenheit = lambda c : c * 9/5 + 32
print(f"Fahrenheit {fahrenheit(96)}")
