class mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("calculating Price")
mobile().purchase()
mobile().purchase()
m1=mobile()
print(m1)
