# 1. if-else shorthand
nums = [ 1, 2,3 ,4,6,7]
print([f"{n} is Even" if n % 2 == 0 else f"{n} is odd" for n in nums])

# 2. Lambda if else
max = lambda m1, m2 : m1 if m1>=m2 else m2
print(f"{max(7, 2)} is greater")

num = lambda n: f"{n} is Even" if n % 2== 0 else f"{n} is odd" 
list = [1,7, 8, 17, 6]
result = [num(n) for n in list]
print(result)

#List comprehension with lambda function

#square 
nums = [3, 4, 6, 7]
square = lambda sqr: [n ** 2 for n in nums]
print(square(nums))

# #chaining

num = -1
print("Positive" if num > 0 else "Neutral" if num == 0 else "Negative")

nums = [90, 0 , -1 , 5]
condition = ["Positive" if n > 0 else "Neutral" if n == 0 else "Negative" for n in nums]
print(condition)