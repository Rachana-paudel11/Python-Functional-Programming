#Returning a function from a function
def outer():
    print("Hi")
    def inner():
        print("Joe")
    return inner

inner = outer() #here, inner is a alias for outer(), which returns inner()
inner() #Now local function can be easily execute
