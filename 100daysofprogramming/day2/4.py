# score = 0 
# score += 1
# print(score)

score = 0
height = 1.8
isWinning = True 

print(f"your score is {score}, your height is {height}, your winning is{isWinning}")

#how many days,weeks months we have left if we live 90 year old
# 1 year = 365 days,52weeks,12 month
age =input("what is your current age?")
age_year_int= int(age)
years_remaining = 90 - age_year_int
days_remaining = years_remaining *365
months_remaining = years_remaining*12
weeks_remaining = years_remaining *52
print(f"you have {days_remaining} days, {weeks_remaining} weeks , and {months_remaining} left")