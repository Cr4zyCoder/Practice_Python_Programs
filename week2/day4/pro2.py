#binary search in python
def binarySearch(array, x, low,high):
    while low <= high:
        mid = low + (high-low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array = [10, 9, 3, 4, 5, 8]
x = 90
result =  binarySearch(array, x,0,len(array)-1)
if result != -1:
    print("Element found at index " + str(result))
else:
    print ("Not found")