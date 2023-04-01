# Wecare insurance company wants to calculate premium of vehicles.
#-->vehicles are of teo types - "Two Wheeler" and "Four Wheeler" Each vehicle is identified by vehicle id,type,
# cost and premium amiunt.
# -->Premium amount is 2% of the vehicle cost for two wheelers and 6% of the vehicle cost for four wheelers.
# Calculate the premium amount and display the vehicle details.
# write a python program to implement the classs choseen with its attributes and methods.?
# Note:
# Consider all instance variables to be private and methods to be public 
# Include getter and setter for all the  variables
# Display appropriate error message, if the vehicle type is invalid
# Perform case sensutuve string comparision
# Represent few objects of tye class, initialize instance variables using setter methods, invoke appropriate 
# methods and test your program
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
        
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
        
    def get_vehicle_id(self):
        return self.__vehicle_id
        
    def get_vehicle_type(self):
        return self.__vehicle_type
        
    def get_vehicle_cost(self):
        return self.__vehicle_cost 
        
    def get_premium_amount(self):
        return self.__premium_amount
        
    def calculate_premium(self):
        if self.__vehicle_type=="two wheeler":
            self.__premium_amount=self.__vehicle_cost*0.02
        elif self.__vehicle_type=="four wheeler":
            self.__premium_amount=self.__vehicle_cost*0.06
    
    def display_vehicle_details(self):
        self.calculate_premium()
        print("the vehicle id is : ",self.__vehicle_id)
        print("The vehilcle type :" ,self.__vehicle_type)
        print("The vehicle cost is:",self.__vehicle_cost)
        print("The vehicle premium is:",self.__premium_amount)
obj=Vehicle()
obj.set_vehicle_cost(15000)
obj.set_vehicle_id(123)
obj.set_vehicle_type("two wheeler")
obj.set_premium_amount(8400)
obj.display_vehicle_details()