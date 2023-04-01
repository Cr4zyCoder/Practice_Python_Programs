#WAP which accepts a sentence and finds the number of letters and digits in the sentence. It should return a list in which the first value 
#should be letter count and second value should be digit count. Ignore the spaces or any other special character in the snetence.
# def count_letters_digits(sentence):
#     letter_count = 0
#     digit_count = 0
#     for char in sentence:
#         if char.isalpha():
#             letter_count += 1
#         elif char.isdigit():
#             digit_count += 1
#     return [letter_count, digit_count]

# sentence = "I am 20ECE038"
# result = count_letters_digits(sentence)
# print(result) 
#wap function find_pairs_of_numbers() which accepts a list of positive integers with no repetitions and returns count of 
#pairs of numbersin the list that adds up to n. The function should return 0 , if no such oairs are found in the list.

# def find_pairs_of_numbers(numbers, n):
#     count = 0
#     for i, num1 in enumerate(numbers):
#         for j, num2 in enumerate(numbers[i+1:]):
#             if num1 + num2 == n:
#                 count += 1
#     return count
# numbers = [1, 2, 3, 4, 5]
# print(find_pairs_of_numbers(numbers, 6))


def find_pairs_of_numbers(numbers, n):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == n:
                count += 1
    return count
numbers = [1, 2, 7, 4, 5, 6, 0, 3]
print(find_pairs_of_numbers(numbers, 6))