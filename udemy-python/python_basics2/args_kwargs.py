# args **kwargs

# def super_func(*args, **kwargs):
#     print(kwargs)
#     return sum(args) 

# print(super_func(1,2,3,4,5,num1=5,num2=12))

def super_func(name, *args, i='hi', **kwargs):
    total = 0
    print(kwargs)
    for items in kwargs.values():
        total += items
    return name, sum(args) + total

print(super_func('Andy',1,2,3,4,5,num1=5,num2=12))

#rule: params, *args, default parameters,**kwargs
