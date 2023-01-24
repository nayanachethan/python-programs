#tuple - are like list , unlike list they are immutable

my_tuple =(1,2,3,4)
print(my_tuple[2])
print(5 is my_tuple)

user = {
    (1,2): [1,2,3] ,
    'greet': 'hello',
    'age':30
}

# # print(user.items())
# print(user[(1,2)])
# my_tuple =('a','b','c','d')
# new_tuple = my_tuple[1:3]

# print(new_tuple)


my_tuple =(1,2,3,4,3)

print(my_tuple.count(3))
print(my_tuple.index(3))
print(len(my_tuple))
