# Write a python program that accepts a text and displays a 
# string which contains the word with the largest frequency
#  in the text and the 
# frequency itself separated by a space.
# Rules:
# The word should have the largest frequency.
# In case multiple words have the same frequency, then choose 
# the word that has the maximum length.
# Assumptions:
# The text has no special characters other than space.
# The text would begin with a word and there will be only a 
# single space between the words.
# Perform case insensitive string comparisons wherever 
# necessary.

def find_most_frequent_word(text):
    words = text.lower().split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    max_freq = 0
    max_length = 0
    max_word = ""
    for word, freq in freq_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_length = len(word)
            max_word = word
        elif freq == max_freq and len(word) > max_length:
            max_length = len(word)
            max_word = word
    return f"{max_word} {max_freq}"

text = "The quick brown fox jumps over the lazy dog. The dog slept on the       car. suddenly it rained and the dog got wet"
most_frequent_word = find_most_frequent_word(text)
print(most_frequent_word)
