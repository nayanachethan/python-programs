# parameters #arguements
# Default parameters

# func should one thinh really well
# should return something
# def say_hello():
#   print('helloooo')

# # say_hello()

# def say_hello(name,emoji):
#       print(f'helooooo {name} {emoji}')
      
# say_hello('nayan',':)' )

# return 
# def sum(num1, num2):
#     # print('hii')
#    return num1 + num2
# total= 15    
# print(sum(4,total))

def sum(num1, num2):
    def another_func(num1,num2):
     return num1 + num2
    return another_func                                                                  
   
# total = sum(10,20)
# print(total)
 
total = sum(10,20)
print(total(10,20))