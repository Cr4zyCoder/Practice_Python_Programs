# Write a python program to help an airport manager to generate
#  few statistics based on the ticket details available for a 
# day.
# Go through the below program and complete it based on the comments mentioned in it.
# Note: Perform case sensitive string comparisons wherever necessary.
# '''



# #Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
# #Note: flight_no has the following format - "airline_name followed by three digit number

# #Global variable
# ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number"

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(flight_no):
   
    passengers = []
    for ticket in ticket_list:
        if ticket.startswith(flight_no):
            passengers.append(ticket.split(":")[-1])
    return passengers

def find_passengers_destination(destination):
    
    passengers = []
    for ticket in ticket_list:
        if ticket.split(":")[2] == destination:
            passengers.append(ticket.split(":")[-1])
    return passengers

def find_passengers_per_flight():
    
    passenger_count = {}
    for ticket in ticket_list:
        flight_no = ticket.split(":")[0]
        passenger_count[flight_no] = passenger_count.get(flight_no, 0) + 1
    sorted_passenger_count = sorted(passenger_count.items(), key=lambda x: x[1], reverse=True)
    for flight, count in sorted_passenger_count:
        print(f"{flight}: {count} passengers")

def sort_passenger_list():
    
    passengers = set()
    for ticket in ticket_list:
        passengers.add(ticket.split(":")[-1])
    return sorted(list(passengers))

print(find_passengers_flight("AI"))

print(find_passengers_destination("LON"))


find_passengers_per_flight()

print(sort_passenger_list())

