#write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome 
#grreater than the  given number. sample input 99 output 101

def nearest_palindrome(num):
    num += 1
    while str(num) != str(num)[::-1]:
        num += 1
    return num
    
num=int(input("Enter a number: "))
print(nearest_palindrome(num))