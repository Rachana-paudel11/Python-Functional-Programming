num = 10 #Global Variable
def display():
    
    #global num #uncomment this line to get unboundlocalerror
    num = num + 5 #this is local variable have to make it global variable 
    print(num)
display()