# Write a function add_numbers(a, b, c) that returns the sum of three numbers.
def add_numbers(a, b, c):
    return a + b + c
print(f"Sum of three numbers: {add_numbers(1, 2,4)}")

#Write a function student_info(name, course) that prints the student’s details using keyword arguments.
def student_info(name, course):
    return f"\nStudent's Name: {name}\nCourse: {course}"
print(student_info(name = "John Doe", course = "Ethical Hacking"))

# Write a function greet(name="Guest") that prints a greeting.
def greet(name="Guest"):
    return f"\nHello, {name}"
print(f"\nUse of default param: {greet()}")
print(f"{greet('Rachana')}")

#Write a function that takes any number of numeric arguments and returns their average.

def ave_rage(*nums):
    add = sum(nums)
    length = len(nums)
    average = add/length
    return average
print(ave_rage(10,20,30))

# 🔹 Q5. Keyword Variable-Length Arguments (**kwargs)
# Write a function display(**info) that prints keys and values in this format:
def details(**info):
    for keys, values in info.items(): 
        print(f"{keys}: {values}")
details(name = "Rachana", age = 21)

#Write a program with a global variable x = 10.
#Inside a function, define another variable x = 20 and print both using globals() and locals().
x = 10
def test():
    x = 20
    print(f"Inside Function : {locals()['x']}")
    print(f"Accesing global Function : {globals()['x']}")
    
test()

#Write a lambda function that checks whether a number is positive, negative, or zero.
nums = [ 1, 0 , -1]
determine = lambda n : ["Positive" if n > 0 else "Neutral" if n == 0 else "Negative" for n in nums]
print(determine(nums))

#Write a function outer() that defines a nested function inner() and returns it.
def outer():
    def inner():
        return f"Inner function executed!"
    return inner
inner = outer()
print(f"{inner()}")

#Write a function show_details(name, course="IT", *hobbies) that displays a student’s details and hobbies.
def show_details(name, *hobbies, course="IT"):
    print(f"Name: {name}\nCourse: {course}\nHobbies: {hobbies}")
show_details("Rachana","Dancing","signing")