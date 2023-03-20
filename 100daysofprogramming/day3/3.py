
year=int(input("which year do you want to check?"))


if year%4 == 0 :
    if year%400 == 0 and year%100 == 0:
        print('Leap')
    elif year%400 == 0:
        print('Leap')
    elif year%100 == 0:
        print('Not Leap')
    else:
        print('Leap')
else:
    print('Not Leap')


# if year % 4==0:
#     if year %100==0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")


    

    





