# A teacher is in the process of generating few reports based on the marks scored by the students of her class in a
# project in assessment.
# Assume that the marksof her 10 students are available in a tuple, the marks are out of 25.
# Write a python program to implement the following functions:
# 1. find_more_than_average(): Find and return the percentage of students who have scored more than the average 
# mark of the class.OverflowError
# 2. generate_freque : find how many students have scored the same works. The results should be populated in a 
# listand returned.
# 3. sort_marks() : Sorncy()t the marks in the increasing order from 0 to 25. The sorted values should be populated in a
# list and returned

# marks = (18, 21, 15, 22, 17, 20, 16, 19, 20, 23)

# def find_more_than_average():
#     avg = sum(marks)/len(marks)
#     count = sum(1 for mark in marks if mark > avg)
#     return count/len(marks) * 100

# def generate_frequency():
#     freq = [0]*26 # initialize a list with 26 elements set to zero
#     for mark in marks:
#         freq[mark] += 1
#     return freq

# def sort_marks():
#     return sorted(marks)

# print("Percentage of students who scored more than average:", find_more_than_average())
# print("Frequency of marks:", generate_frequency())
# print("Sorted marks:", sort_marks())
marks = (18, 21, 15, 22, 17,17, 20, 16, 19, 20, 23)

def find_more_than_average():
    avg = sum(marks)/len(marks)
    count = 0
    for mark in marks:
        if mark > avg:
            count += 1
    return (count/len(marks)) * 100

def generate_frequency():
    freq = {}
    for mark in marks:
        if mark in freq:
            freq[mark] += 1
        else:
            freq[mark] = 1
    return freq

def sort_marks():
    return sorted(marks)

print("Percentage of students who scored more than average:", find_more_than_average())
print("Frequency of marks:", generate_frequency())
print("Sorted marks:", sort_marks())
