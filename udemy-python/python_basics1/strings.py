#strings
print(type("hi hello there!"))
username = "supercoder"
password = 'supersecret'
long_string = '''
WOW 
awesome
'''
print(long_string)

first_name = 'Nayana'
last_name = 'karanth'
full_name = first_name + last_name
print(full_name)

full_name = first_name + ' ' + last_name
print(full_name)

print(type(str(100)))
print(type(int(str(100))))

a= str(100)
b= int(a)
c= type(b)
print(c)
# type conversion

# Escape Sequence
weather = "It\'s  \"kind of\"  sunny"
print(weather)
weather = "\t It\'s  \"kind of\"  sunny \n hope you had a good day!"
print(weather)

#formatted strings
name = 'johny'
print('hi ' + name)

name = 'johny'
age = 45
print('hi ' + name+  '. you are ' +  str(age) + ' years old')

name = 'johny'
age = 45
print(f'hi {name}. you are {age} years old')

print('hi {}. you are {} years old'.format('johny','45'))
print('hi {new_name}. you are {age} years old'.format(new_name='sally', age=100))

# string index
selfish = '01234567'
        #  01234567
        #string slicing
# [start:stop:stepover]
print(selfish[::-2])

#immutability
#cannot reassign part of the string
selfish = '01234567'
selfish = '5'
print(selfish)

n = 'chethan'
print(n)
n = 'j'
print(n)

# built in function and methods
greet = 'hellooooo'
print(greet[0:len(greet)])

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.count('or'))
print(quote.replace('not', 'me'))
print(quote)

#booleans

name = 'chethan'
is_mad = False
is_mad = True
print(bool(1))

#type conversion

birth_year = input('what year were you born? ')
age = 2022 - int(birth_year)
print('Your age is: ', age)

#commenting fundamentals
