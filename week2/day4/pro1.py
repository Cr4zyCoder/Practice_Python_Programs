#linear search inpython
def linearsearch (array,n,x):
    for i in range(0,n):
        if (array[i]==x):
            return i
    return -1
array = [2,4,0,5,9]        
x=4#key
n = len(array)
result = linearsearch(array,n,x)
if (result == -1):
    print("Element found at index: ", result)
else:
   print("Element not found") 