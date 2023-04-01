class Customer:
    def __init__(self, cust_id, name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def set_balance(self,amount):
        if amount <5000 and amount > 0:
            self.__wallet_balance += amount
    def get_wallent_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Gopal",24,1000)
print(c1.get_wallent_balance())
c1.set_balance(5000)
print(c1.get_wallet_balance())