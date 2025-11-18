# Variable length positional Arguments : *Args
def calculate(*nums): #nums now internally acts as tuple
    sum = 0
    for n in nums:
        sum = sum + n
    return sum
print(calculate(1,2))
print(calculate(1,2,3))
print(calculate(1,2,3,4))

print("*" * 100)
#Variable length keyword arguments: **kwargs
def calc(**numbers):
    # add = 0
    # for n in numbers.values():
    #     add = add + n
    return sum(numbers.values())
       
    
print(calc(n1= 10, n2 = 20))
print(calc(n1= 10, n2 = 20, n3 = 30))
    
print("*" * 100)

#Mixing variable length positional and keyword argument
def calculate(*nums,**numbers): #must be in order first variable length postional then variable length arguments
    print(nums)
    print(numbers)
calculate(10, 20 , 20, n1= 10 , n2 = 40 , n3 = 60) 