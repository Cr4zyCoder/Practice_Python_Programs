#Rate for Adults : Rs 37550.0
#Rate for chile : 1/3rd of the rate per adult
#Service TAx: 7% of the ticket 
#holiday : 10% discount
adult=int(input("Enter the number of adults: "))
children= int(input("Enter the number of children: "))
price1=adult*37550.0
price2=children*(37550.0/3)
t_price=price1+price2
ta_price=t_price+(t_price%7)
final_price=ta_price-(ta_price%10)
print("The Toatal cost of Flight Ticket is: ",final_price,"Rs")

price=((((adult*37550.0)+(children*(37550.0/3)))*1.07)*0.90)