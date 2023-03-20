# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = weight/(height**2)
# print(bmi)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) /float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)