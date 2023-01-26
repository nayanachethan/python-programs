is_old = False
is_licenced = False

if is_old and is_licenced:
    print('you are  old enough to drive, and you have a license!')

elif  is_licenced:
    print('you can drive now!')

else:
    print('you are not of age!')   

print('okokok')

# Ternary operator
# conditional expression - evaluates something whether true or false

# condition_if_true if condition else condition_if_false
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

# Short circuiting 
is_friend = True
is_User= False
if is_friend or is_User:

   print('best friends forever')

#Logical operators 
print(9<0)
print('a' > 'A')
print( 0 != 1)

is_magician = True
is_expert = False

if is_magician and is_expert:
    print('you are master magician!')

elif  is_magician and not is_expert:
    print('atleast you are getting there!')

elif not is_magician:
    print('you need magic powers!') 


print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print(True is True)
print('' is 1)
print([] is 1)
print(10 is 10)
print([] is [])
