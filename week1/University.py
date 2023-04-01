# # A university wants to automate their admission process. 
# # students are admitted based on marks scored in a qualifying exam.
# # A studentis identified by student id, age and marks in qualifying exam.
# # Data are valid, if:
# #     age is greater than 20
# #     Marks is between 0 and 100
# #     A student qualifies for admission, if
# #     age and marks are valid and marks is 65 or More
# # Write a python program to represnt the students seeking admission in the university?

# Rules to follow
# the details of student class are given below
# Class name: Student
# --Atributes:(private)
#     student_id
#     marks
#     age
# methods
# (public)        __init__() create and initialize all instance
# validate_marks()
# validate_age()
# check_qualifications()
#  validate marks and age,
# if valid, check if marks is 65 or More
# if so returns True
# else returns False
# setter methods Include setter methods for all instance variables to set its values
# getter methods include getter methods for all instance variables to get its all values
# continuing with the pevious scenario, a student eligible for admission has 
# to choose a course and pay the fees for it. If they have scored more than 85 
# marks in qualifying exam, they get 25% discount on fees
class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None

    def validate_marks(self):
        if 0 <= self.__marks <= 100:
            return True
        else:
            return False

    def validate_age(self):
        if self.__age >= 20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65:
                print("Student is eligible for admission")
                
                return True
            else:
                print("Student is not Eligible for admission")
                return False
        else:
            print("Student is not Eligible for admission")
            return False
    
    def check_scholarship(self):
       if self.__marks >=85:
           print("Student is eligible for 25% Scholarship")
           return True
       else:
           print("Student is not Eligible for Scholarship")
           return False
           
    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks
    
    def get_age(self):
        return self.__age
    
    def display_student(self):
        print("Student ID: ", self.__student_id)
        print("Marks: ", self.__marks)
        print("Age: ", self.__age)

obj = Student()

obj.set_student_id(15)
obj.set_marks(78)
obj.set_age(20)
obj.check_qualification()
obj.check_scholarship()
obj.display_student()