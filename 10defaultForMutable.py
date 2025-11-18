def add_item(name, employee_data = []):
    employee_data.append(name)
    print("Update data is:", employee_data)
    
add_item("Rachel")
print(add_item.__defaults__)
add_item("John")
print(add_item.__defaults__)   
add_item("Doe")