#logical operators

print("welcome to rollar coastar ride")
height = int(input("what is height in cm?"))
bill=0

if height>=120:
    print("you can take the ride")

age= int(input("what is your age? "))

if age<12:
        bill=5
        print("child tickets are $5")
elif age <= 18:
        bill=10
        print("youth tickets are $10")   
elif age>=45 and age <=35:
      print("Everything is going to be OK.Have a free ride on us!")
else:
        bill=12
        print("adult tickets are $12")

want_photo =input("do you want a photo to be clicked? Y or N.") 
if want_photo=="Y":
    bill +=3
    print(f"your final is {bill}")

else:
      print("Sorry better luck next time")



