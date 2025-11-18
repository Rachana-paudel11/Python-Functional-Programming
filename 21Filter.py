#filter(func, sequence) - It is a higher oreder function
# Only returns true values

data = [3, 11, 7, 25, 40, 9]
def greater(n):
    if n>10:
        return True
    else:
        return False
    
result = list(filter(greater, data))
print(f"Greater than 10: {result}")

#lambda
greater_lambda = list(filter(lambda x: x> 10, data))
print(f"Greater than 10: {greater_lambda}")

words = ["cat", "tiger", "lion", "rat"]
def checker(word):
    for char in word:
        if char == "t":
            return True
    else:
        return False
    
result = list(filter(checker, words))
print(f"Words which includes 't': {result}")

lambda_checker = list(filter(lambda word: "t" in word, words ))
print(f"Words which includes 't': {lambda_checker}")

#filter vowels from given string

str1 = input("Enter the string: ")
vowels_letter = ['a','e','i','o','u']
def vowels(ch):
    if ch in vowels_letter:
        return True
    

checker = list(filter(vowels, str1))
print(checker)


data = {'Rachana' : 98, 'Archana': 100, 'Samyog': 100, 'John': 45, 'Doe': 56}

def marks(student):
    return data[student] > 90
    
checK_marks = list(filter(marks, data))
print(checK_marks)
