#Factorial of a number 
num = 7
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1) #recusrive call
factorial = fact(num)
print(f"Factorial of {num}: {factorial}")

# Find the Fibonacci number using recursion
# Series: 0,1,1,2,3,5…

def fibo(n, a = 0, b = 1):
    if n == 0:
        return
    print(a, end = " ")
    fibo(n - 1, b, a + b) 
fibo(5)

#count the digit in a number
number = 12121434
def count_digit(n):
    if n == 0:
        return 0
    return 1 + count_digit(n//10)
print(f'\nTotal count {count_digit(number)}')

#Palindrome
number = 1221  

def reversed_number(n , rev = 0):
    if n == 0:
        return rev
    temp = n % 10
    return reversed_number(n//10, rev * 10 + temp)

def is_palin(n):
    if n < 0:
        return False
    print(f"palindrome")
is_palin(number)