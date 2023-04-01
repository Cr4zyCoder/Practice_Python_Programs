# A bank has many customers and each customer has a bank account
# There are also privileged customers 
# who can earn bonus points for each of their transaction. 
# This scenario is depicted through the below class diagram.
# 30 min

# Customer
# - customer_id
# - customer_name
# - age
# - account
# __init__(customer_id, customer_name, age, account)
# + withdraw(amount)
# + take_card()
# + get_customer_id()
# + get_customer_name()
# + get_age()
# + get_account()
# Account
# - account_type
# - balance
# - min_balance
# __init__(account_type,balance,min_balance)
# + get_account_type()
# + get_balance()
# + get_min_balance()
# + set_balance(balance)
# PrivilegedCustomer
# - bonus_points
# __init__ (customer_id, customer_name, age, account, 
# bonus_points)
# + withdraw(amount)
# + get_bonus_points()
# - increase_bonus()
# OverdrawException
# LimitReachedException

# RULES TO FOLLOW
# ================
# Customer:
# withdraw(amount): This method should reduce the account balance based on the amount withdrawn. 
# Raise the following exceptions based on the given conditions.
# OverdrawException - If the amount to be withdrawn is greater than account balance.
# LimitReachedException - If the balance amount is less than minimum account balance.
# take_card(): Displays the message "Take card out from the ATM".
# PrivilegedCustomer:
# increase_bonus(): If the account balance is greater than 1000, increase the bonus points by 10, else increase it by 2.
# withdraw(amount): Invoke the parent class withdraw() method and increase the bonus points by calling increase_bonus() method, if no exceptions occured.
# If exceptions occur, display relevant messages. Ensure that the card is taken out from the ATM under any situation.

# Write a Python program to create a new PrivilegedCustomer with below details:
# Customer Id: 100
# Customer Name: Gopal
# Age: 43
# Bonus Points: 100
# Account Type: Savings
# Account Balance: 1000
# Account minimum: 500

# The customer should be able to withdraw money and also display the bonus points of the customer after the withdraw.
# ------------------------------------------

# A company is in the process of providing annual hike to its employees based on incentives and performance of the employee.
# A partial python program has been written for the above requirement, complete the code by using the information and part of class diagram given below:


# RULES TO FOLLOW
# =================
# Class Description:
# The program has three classes – Company, Employee and PermanentEmployee. Company and Employee classes are already coded for you. Refer starter code.

# Employee class:
# Every employee is given a performance rating (1-3) at the end of every year
# Last five year's performance rating of an employee is stored in the attribute, performance_list
# Refer table for example and interpretation of data in performance_list, assuming current year is 2015
# Permanent Employee class:
# identify_performance_hike():
# Permanent employees are eligible for performance hike based on their last three years performance as given in table
# Identify the hike % and return it. If hike is not applicable, return None
# identify_job_level_hike():
# Permanent employees are eligible for hike based on job level
# Identify job level based hike using the information provided in the Company class and return it. If hike cannot be identified, return None
# identify_incentive():
# Permanent employees are eligible for company level, employee level and permanent employee level incentives
# Calculate total incentive (in Rs) and return it
# calculate_salary(): Calculate total salary
# Implement it in the same way as it is implemented in Employee class
# Note: Perform case sensitive string comparison 
# For testing:
# Create objects of Company class and PermanentEmployee class
# Invoke calculate_salary() on PermanentEmployee object
# Display the details of the employee


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee:
    employeelist=list()
    def __init__(self,empid,empName,empDes,empSal):
        self.empid=empid
        self.empName=empName
        self.empDes=empDes
        self.empSal=empSal
    def addNewEmployee(self):
        Employee.employeelist.append(self)
    def getEmplist(self):
        return Employee.employeelist
    def getEmpById(self,empid):
        for emp in Employee.employeelist:
            if(emp.getempid(empid)==empid):
                return emp
        return False
    def setempid(self,empid):
        self.empid=empid
    def getempid(self,empid):
        return self.empid
    def setempName(self,empName):
        self.empName=empName
    def getempName(self,empName):
        return self.empName
    def setempDes(self,empDes):
        self.empDes=empDes
    def getempDes(self,empDes):
        return self.empDes
    def setempSal(self,empSal):
        self.empSal=empSal
    def getempSal(self,empSal):
        return self.empSal
    def __str__(self):
        return "%d %s %s %d"%(self.empid,self.empName,self.empDes,self.empSal)
choice=1
employee=Employee(0,"","",0.0)
while choice>=1 and choice<=3:
    print("\n\n1.Add new employee\n 2.Get all employee list\n 3.Get Employee by Id\n\n")
    choice=int(input("Enter your choice"))
    if(choice==1):
        empid=int(input("Enter Employee id:"))
        empName=input("Enter Employee Name:")
        empDes=input("Enter Employee Designation:")
        empSal=float(input("Enter Employee Salary"))
        emp=Employee(empid,empName,empDes,empSal)
        emp.addNewEmployee()
    elif(choice==2):
        print("\n")
        for emp in employee.getEmplist():
            print(emp)
    elif(choice==3):
        empid=int(input("Enter Employee id:"))
        empid=employee.getEmpById(empid)
        if (emp==False):
            print("\n SORRY Employee not found for Id!!!",empid)
        else:
            print(emp) 








