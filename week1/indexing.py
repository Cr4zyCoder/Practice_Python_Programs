#write aprogram function which accepts a string and returns a string made of the first 2 and the last 2 characters
# of the given string. If the string is less than 2, return -1
def first_last_chars(string):
    if len(string) < 2:
        return -1
    else:
        return string[0:2] + string[-2:]
print(first_last_chars("Hello GIET"))