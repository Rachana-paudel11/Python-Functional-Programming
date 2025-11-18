#default Arguments: the parameter having default value
def calculate(items, currency = "Rs/-"):
    print(f"{sum(items)} {currency}")

list = [1, 2, 3]
calculate(list)