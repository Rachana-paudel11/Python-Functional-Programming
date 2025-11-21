#Direct Recursion: when function call itself directly inside of its own body
def natural(n):
    if n == 0: #stopping condition
        return
    print(n, end=" ")
    natural(n - 1) #recursive call(direct recursion)
natural(10)
print(50*"__")

#Indirect Recursion: when a function call another function, which calls the first
def num(n):
    if n <= 0:
        return
    print(n, end=" ")
    num1(n-1)
def num1(n):
    print(n, end=' ')
    num(n-1)
    
num1(10)