#Mixxing multiple types of arguments
'''
    Must follow this order
        ' positional arguments > variable length positional arguments > 
        Keyword arguments > Default argument > variable length Keyword arguments'

'''
def details(name, *city, age, job ="unemployed", **skills):
    print("Name: ", name)
    print("City: ", city)
    print("Age: ", age)
    print("Skills: ", skills)
    print("Job: ", job)
    
    
details('Rachana', "Butwal", "Kathmandu", "Bhairahawa", age = 21, s1 = 'c#', s2 = 'Excel', s3 = "python")