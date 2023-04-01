#erite a pythnon program to add ing at the end of a given string and return the new string
# if the given string already ends with ing then add ily.
# if the length of the given string is less than 3 leave it
def first_last_chars(string):
    if len(string) < 3:
        return string
    elif string[-3:]== "ing":
        return string + "ly"
    else:
        return string + "ing"
print(first_last_chars("He"))