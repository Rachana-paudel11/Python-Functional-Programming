 #Nested Lambda Function
 
 
#Nested Normal function
'''def outer():
    def add(a, b):
        return a + b
    return add
add = outer()
print(add(3,4)) '''

#Nested Lambda Function
'''
def outer():
    add = lambda a , b : a + b
    return add
add = outer()
print(add(5,6))
'''

'''
def outer():
    return lambda a, b : a + b
add = outer()
print(add(3, 4)) '''

outer = lambda : lambda a , b : a + b
add = outer() 
print(add(7, 8))

 