def name():
    fn = input("Enter your first name: ")
    ln = input("Enter your last name: ")
    full_name = fn + " " + ln
    return full_name

def display_name(f1):
    print(f1())
display_name( name) # argument here, is a reference of a function
'''
passing arguments as a reference - to pass whole fumction object
'''




    