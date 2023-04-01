# The owner of a BakeHouse wants to keep track of the tables 
# that are occupied in his cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is occupied, it must be added to the occupied_table_list and when a customer leaves, the corresponding table must be removed from the list.

# BakeHouse
# - occupied_table_list
# _init_()
# + get_occupied_table_list()
# + allocate_table()
# + deallocate_table(table_number)
# Write a python program to implement BakeHouse class. 
# Represent occupied_table_list using an appropriate data 
# structure.


# Note: Table numbers should be maintained in ascending order in the occupied_table_list.


# Tables should be allocated and de-allocated as mentioned in the example below:

# Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, he should be allocated table 5 and the table list should be accordingly updated. If now customer at table 2 leaves, table list should be accordingly updated and the next new customer should be
class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []

    def get_occupied_table_list(self):
        return self.occupied_table_list

    def allocate_table(self):
        if len(self.occupied_table_list) == 0:
            self.occupied_table_list.append(1)
        else:
            for i in range(len(self.occupied_table_list)):
                if i == len(self.occupied_table_list) - 1:
                    self.occupied_table_list.append(self.occupied_table_list[i] + 1)
                elif self.occupied_table_list[i+1] - self.occupied_table_list[i] > 1:
                    self.occupied_table_list.insert(i+1, self.occupied_table_list[i] + 1)
                    break

    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)
        else:
            print("Table not found in occupied table list")

# Creating an instance of the BakeHouse class
bh = BakeHouse()

# Allocating tables 1, 2, 3 and 4
bh.occupied_table_list = [1, 2, 3, 4]

# Displaying the list of occupied tables
print("Occupied tables:", bh.get_occupied_table_list())

# Allocating a new table
bh.allocate_table()

# Displaying the updated list of occupied tables
print("Occupied tables:", bh.get_occupied_table_list())

# De-allocating table 2
bh.deallocate_table(2)

# Displaying the updated list of occupied tables
print("Occupied tables:", bh.get_occupied_table_list())

# Allocating a new table
bh.allocate_table()

# Displaying the updated list of occupied tables
print("Occupied tables:", bh.get_occupied_table_list())
