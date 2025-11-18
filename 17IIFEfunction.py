'''
In python, normal function can't be modify to IIFE function just like in Javascript.But, can be applied to lambda function
IIFE stands for Immediately Invoked Function Expression.

'''
addition = (lambda a , b: a + b)(3,4)
print(f"IIFE function for addition: {addition}")

increment = (lambda n : n + 1)(int(input("Enter any number: ")))
print(f"IIFE for increment: {increment}")