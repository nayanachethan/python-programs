print("welcome to python pizza deliveries!")
size=input("what size pizza do you want? S,M or L")
add_pepperoni=input("Do you want to add pepperoni? Y or N")
extra_cheese=input("Do you want extra cheese? Y or N")
bill=0

if size=="S":
    bill+= 5
elif size =="M":
    bill+= 10
elif size == "L":
    bill+= 20

if add_pepperoni =="Y":
    if size=="S":
      bill +=2
else:
    bill+=3

    if extra_cheese=="Y":
        bill+=1

print(f"Your final bill is ${bill}")
