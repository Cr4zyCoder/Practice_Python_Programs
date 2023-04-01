#a train is identified by its name and list of compartments. The compartments 
# are identified by its name, total seating capacity and the number of passengers
# Implement the class Train as given in the class diagram.
# Train
# - train Name
# - compartment_list
# - __init__(train_name, compartment_list)
# +get_train_name()
# +get_compartment_list
# +count_compartments()
# +check_vacancy

# write a python program to implemenet thr following:
# count_compartments()-returns the total number of compartments in the train?
# checl_vacancy()-returns the count of the compartments in which more than 50% of 
# the seats are vacant
# Note: Compartment list is maintained as a linked list where data in each node
# refers to a compartment 
# A train is identified by its name and list of compartments. The copartments are



class train:
    def __init__(self, train_name, compartment_list):
        self.train_name = train_name
        self.compartment_list = compartment_list
        self.count_compartments()
    def count_compartments(self):
        self.count = len(self.compartment_list)
        def get_train_name(self):
            return self.train_name
        def get_compartment_list(self):
            return self.compartment_list
        def count_compartments(self):
            return len(self.compartment_list)
        def check_vacancy(self):
            pass
