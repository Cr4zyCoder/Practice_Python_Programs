def calculate_coins(x, y, amount):
    total = x*5 + y*1 
    if total < amount:
        return 1 

    k = amount // 5 
    remaining = amount % 5 
    if remaining > y:
        return 1 
    return k, remaining 

# Example usage
x = 2 # number of 5 rupee coins
y = 11 # number of 1 rupee coins
amount = 19 # amount to pay

result = calculate_coins(x, y, amount)
if result == 1:
    print("Exact change is not possible.")
else:
    k, remaining = result
    print(f"Use {k} 5 rupee coins and {remaining} 1 rupee coins.")
