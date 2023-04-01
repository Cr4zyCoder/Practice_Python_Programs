#INput a string of comma separated numbers, the number 5 and 8 are present in the list. Assume that 8 
# always comes after 5.
# case1: num1 = add all the numbers which do not lie between 5 and 8 in the output
# case2: num2 = number formed by concatenating all numbers from 5 to 8
# output sum of num1 and num2

def sum_num(string):
   
    num_list = string.split(',')

    index_5 = num_list.index('5')
    index_8 = num_list.index('8')

    num1 = sum([int(num) for num in num_list[:index_5] + num_list[index_8+1:]])
    num2 = int(''.join(num_list[index_5:index_8+1]))

    return num1 + num2

string=input("enter a string")
print(sum_num(string))