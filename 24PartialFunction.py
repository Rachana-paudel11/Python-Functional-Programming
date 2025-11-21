#Partial function comes from functools module
# it allows to fix certain no. of arguments of a function and generates a new function
#partial(function_name,arg1, arg2, ....)

from functools import partial

def si(p, t, r):
    return p*t*r
calculate = partial(si,r=0.2) #rate for some institute will be same for each client
print(f"Your simple interest: {int(calculate(p = 500000, t = 2))}")

'''
if there is keyword argument in partial function,
then while passing for main function it must be keyword argument '''

