# #find the number of distinct subarrays in an array of position integers such that the sum of the subarray is an odd integer,
# # two subarray are considered different if they start or end at different index input
# def count_odd_subarrays(arr):
#     count = odd_count = 0
#     n = len(arr)
    
#     # Iterate over all subarrays
#     for i in range(n):
#         for j in range(i, n):
#             # Calculate the sum of the current subarray
#             subarray_sum = sum(arr[i:j+1])
            
#             # If the sum is odd, increment the count of odd subarrays
#             if subarray_sum % 2 == 1:
#                 odd_count += 1
            
#             # Increment the total count of subarrays
#             count += 1
    
#     # Subtract the count of even subarrays from the total count to get the count of distinct odd subarrays
#     distinct_odd_count = odd_count - (count - odd_count)
    
#     return distinct_odd_count
# num1=int(input("Enter a number: "))
# num2=int(input("Enter the 2nd number: "))
# for i in range(num1,num2):
#     print(i)
# def count_and_print_odd_subarrays(arr):
#     n = len(arr)
#     distinct_sums = set()
#     odd_sums = {}
#     for i in range(n):
#         curr_sum = 0
#         for j in range(i, n):
#             curr_sum += arr[j]
#             if curr_sum % 2 == 1:
#                 distinct_sums.add(curr_sum)
#                 if curr_sum in odd_sums:
#                     odd_sums[curr_sum].append(arr[i:j+1])
#                 else:
#                     odd_sums[curr_sum] = [arr[i:j+1]]
#     for sum, subarrays in odd_sums.items():
#         print(f"Subarrays with sum {sum}:")
#         for subarray in subarrays:
#             print(subarray)
#     return len(distinct_sums)

# arr = [1, 2, 3, 4, 5]
# count = count_and_print_odd_subarrays(arr)
# print(f"Total number of distinct odd sums: {count}")
#-----------------------------------------------------------
n1=int(input("Enter a value"))
n2=int(input("Enter a value"))
array=[i for i in range(n1,n2+1)]
print(array)
result=[]
for i in range (len(array)) :
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
#result=[array[i:j+1] for i in range(len(array)) for j in range (i,len(array))]#single line code
#print(result)
c=0
for i in result:
    if sum(i) % 2 !=0:
        c+=1
print (c)