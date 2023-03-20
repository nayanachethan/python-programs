# welcome to the tip calculator
# total bill
# what percentage tip would you like to give
# how many people to split the bill
# each person should pay



print("welcome to the tip calculator")
bill = float(input("what is the total bill? $"))
tip = int(input("how much percentage would you like to give , 10,15,20?"))
people =int(input("how many people would like to split the bill?"))
# print("each person should pay ")
# bill_tip = tip/100*bill+bill
# print(bill_tip)

# another way
                
tip_as_percent = tip/100
total_tip_amount = tip_as_percent*bill
total_bill =bill + total_tip_amount 
people_total = total_bill/ people
final_amount =round(total_bill , 2)  
print(f"each person should pay  {final_amount}")          
                
                


