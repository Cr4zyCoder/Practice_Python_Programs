#write a python function, check_double(number) which accepts a whole number and returns TRUE if it satisfies the given conditions.
# 1. the number and  its double should have exactly the same number of digits.
# 2. Both the numbers should have the same digits, but in different order.
# Otherwise it should return FALSE
def check_double(number):
   
    num_str = str(number)
    double_str = str(number * 2)

    
    if len(num_str) != len(double_str):
        return False


    for digit in num_str:
        if digit not in double_str:
            return False


    for digit in num_str:
        if num_str.count(digit) != double_str.count(digit):
            return False

    return True

print(check_double(0))