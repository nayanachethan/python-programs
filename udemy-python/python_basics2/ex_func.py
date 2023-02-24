def highest_even(li):
    evens = []
    for i in li:
        if i%2 == 0:
            evens.append(i)
    print(evens)
    return max(evens)  #try without max

print(highest_even([6,10,2,3,12,4,8,11,13]))

