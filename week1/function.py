def function():
    print("Its a function")
function()
def function2(num1,num2):
    print("num1",num1,"num2",num2)
function2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
print(function3(100,30))
def function4(num1,num2):
    num3=num1+num2
    return num3
print(function4(100,30.08))
def function5(num1,num2):
    num3=float(num1)+num2
    return num3
print(function5('100',30.07))





print("     ")
#3 defaukt arguments
def function3(name,rollno,branch,collegename="Giet"):
    print(name,rollno,branch,collegename)
function3("aditya",11,"Cse")
function3("srikaanth",12,"CST")
print("     ")
#function overloading
def function8(*var):
    for i in var:
        print(i,end=' ')
function8(10,20)
print()
function8(10,20,30,40,50)
print()
function8(10,20,30,40,50,60,70)
print("   ")
def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
        print (sum1)
add(10,20)
print()
add(10,20,30,40,50)
print()
function8(10,20,30,40,50,60,70)


