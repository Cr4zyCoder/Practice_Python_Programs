
def currencycal(amt,curr):
    
    if curr == "Euro":
        print(amt*0.01417)
    elif curr == "BritishPound":
        print(amt*0.0100)
    elif curr == "Australian Dollar":
        print(amt*0.02140)
    elif curr == "Canadian Dollar":
        print(amt*0.20270)
    else:
        print(-1)
print("Enter the currency you would like to convert:")
amt=int(input("Enter the amount you want in INR"))
curr=input("Enter the currency: ")
currencycal(amt,curr)

