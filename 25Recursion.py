#Recursion  - when a function call itself, it is recursuve function.
'''
    syntax: 
    def recursion_name()
        print("Hi")
        recursion_name()
'''
'''
    Python doesn't allow infinite recursion
    default recursion limit: 1000
    
'''

#Getting default limit
import sys
print(f"Default recursion limit: {sys.getrecursionlimit()}")

#Modifying recursion limit
limit = sys.setrecursionlimit(40)
print(f"Modifying recursion limit:")

i = 0
def demo():
    global i
    i = i + 1
    print(f"Limit: {i}")
    print("Hi")
    demo()
demo()