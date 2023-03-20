
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = round(int(weight) / float(height) ** 2)
# if bmi<18.5:
#     print("you are underweight")
# elif bmi>18.5 and bmi<25:
#     print("you have normal weight")
# elif bmi>25 and bmi<30:
#     print("you are overweight")   
# elif bmi<30 and bmi<35:
#     print("you are obese")
# else:
#     print("you are clinically obese")

if bmi<18.5:
    print(f"your bmi is {bmi} , you are underweight.")
elif bmi<25:
    print(f"your bmi is {bmi} , you are normalweight.")
elif bmi<30:
    print(f"your bmi is {bmi} , you are overweight.")
elif bmi<35:
    print(f"your bmi is {bmi} , you are obese.")
else:
    print(f"your bmi is {bmi} , you are clinically obese.")

