'''
    There are two types of functions in Python:
    i. Built-in functions : eg, print(), len(), type()
    ii. User-defined functions
'''

# User-defined function

#Parametarized vs Non-parametarized function


def display(message): #parametarized
    print("Welcome!")
    print(message)
display("Hello world!")
print(50*("-"))
display("My world")


def display_message(): #Non-parametarized
    message = input("Enter any message:")
    print(message)

display_message()

#Parameters and arguments
def si(p,r,t): #Parameters
    print(f"Principle: {p}")
    print(f"Rate: {r}")
    print(f"Time: {t}")
    simple_interest = (p*r*t)/100
    print(f"\nSimple Interest: {simple_interest}")
#function calling 
si(4000,0.5, 3)

    

