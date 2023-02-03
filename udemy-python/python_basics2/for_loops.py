# for loops iterate the collection of items
# for item in (1,2,3,4,5) :
 # for x in ['a' , 'b', 'c'] :
    # print(item, x)
    
# Iterables - list, dictonary,tuple,set,string 
# iterated - one by one check each item in the collection

user =  {
    'name': 'andrie',
    'age': 56,
    'can_swim':True 
 }

for item in user.items():
     print(item)
for item in user.values():
     print(item)
for item in user.keys():     
    print(item)

my_list = [1,2,3,4,5,6,7,8]

counter= 0
for item in my_list:
  counter = counter + item
print(counter)

print(range(0 ,100))