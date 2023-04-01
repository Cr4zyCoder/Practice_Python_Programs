# result=[]
# for i in range(11):
#     result.append(i)
# print(result)

# #list comprehension version--> odd elements

# result=[]
# for i in range(11):
#     if i % 2!=0:
#         result.append(i)
# print (result)

# #list comprehension version --> odd elements
# print([i for i in range (11) if i % 2 !=0])
# # for loop version --> even elements
# result=[]
# for i in range(11):
#     if i % 2!=0:
#         result.append(i)
#     else:
#         result.append(i**2)
# print(result)
# #list comprehension version --> even elements square
# print([i if i % 2 !=0 else i ** 2 for i in range(11)])

mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
result = []

for row in mat:
    row_result = []
    for element in row:
        if element % 2 == 0:
            row_result.append(element ** 3)
        else:
            row_result.append(element ** 2)
    result.append(row_result)

# print the result matrix
for row in result:
    print(row)

#list comprehension
print([element**2 if element % 2 !=0 else element **3 for row in mat for element in row])
print ([[element **2 if element %2 !=0 else element ** 3 for element in row] for row in mat])