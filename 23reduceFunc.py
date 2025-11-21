#reduce(function_name, iterale) - it provides single reduced values

import functools
nums = [1,2,3,4]
def funs(a, b):
    return a * b

print(functools.reduce(funs, nums))

max = functools.reduce(lambda a, b : a if a> b else b, nums)
print(max)