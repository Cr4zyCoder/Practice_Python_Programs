#problem statement: For each number in list_b, get the number and its position (index) in mylist
#are returned list of tuples


mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]

result = []
# for num in list_b:
#     for i, val in enumerate(mylist):
#         if num == val:
#             result.append((num, i))
#             break

# print(result)
# for i in list_b:
#     result.append((i,mylist.index(i)))
# print (result)

# print([(i,mylist.index(i)) for i in list_b])
for i in list_b:
    result.append((i, mylist.index(i)))
print(result)

print([(i,mylist.index(i)) for i in list_b])
result={}
for i in list_b:
    result[i] = mylist.index(i)
print(result)
print({i:mylist.index(i) for i in list_b}) #dict comprehension
 