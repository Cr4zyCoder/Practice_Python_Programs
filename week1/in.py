#write a python program to display all the common characters between two strings. Return -1 if there are no matching characters?
def find_common_characters(in1,in2):
    str=""
    for i in in1:
        if i in in2:
            if i not in str:
                str=str+i
    if(str):
        return str.replace(" ","")
    else:
        return -1
in1=input("enter for in1")
in2=input("enter for in2")
common_characters=find_common_characters(in1,in2)
print(common_characters)

