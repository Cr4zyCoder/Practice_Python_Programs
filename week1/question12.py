# Analyze the below code snippet and identify how ,any objects
# and reference variables will be there at the end of line 9
class Table:
    def __init__(self):
        print(id(self))
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None

dining_table=Table()
i=id(dining_table)
print("dining_table id is" ,+ i)
back_table=Table()
j=id(back_table)
print("back_table is is ",+j)

front_table=back_table
back_table=dining_table

print(id(dining_table),id(back_table),id(front_table))