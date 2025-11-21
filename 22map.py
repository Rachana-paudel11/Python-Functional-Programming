#length of each names
names = ['John', 'Rachel', 'Angelina', 'Doe']
def len_of_name(name):
    # return len(name)
    return name, len(name)

mapped_obj = map(len_of_name, names) #here, mapped_object is object of map
#map object get exhausted after run once
# print(f"Length of the provided name: {map(mapped_obj)}")
for element in mapped_obj:
    print(element)
    print(element[0])
    print(element[0], '-->', element[1])
    
#square of number
nums = [5, 3, 8, 11, 6]
def square(n):
    return n**2
mapped_obj_sqr = map(square, nums)
print(f"Square of {nums}: {list(mapped_obj_sqr)}")

#square of odd nums
def squareoDD(n):
    if n%2 != 0:
        return n**2
    else:
        return n
    
mapped_obj_odd = map(squareoDD, nums)
print(f"Square of odd: {list(mapped_obj_odd)}")

lambda_map = list(map(lambda x: x**2 if x % 2 != 0 else x, nums))
print(f"Lambda : {lambda_map}")

#Passing two arguments in mapped function
marks = [ 60, 70, 80, 90, 100]
bonus = [ 4, 3, 2, 1]
def logic(arg1, arg2):
    return arg1 + arg2
mapped_obj = map(logic, marks, bonus)
for ele in mapped_obj:
    print(ele)