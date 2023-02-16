picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# for image in picture:
#     for pixel in image:
#         if (pixel == 1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')  

fill = '*' 
empty = ' '

def show_tree():
    for image in picture:
        for pixel in image:
            if (pixel):
                print(fill, end ="")
            else:
                print(empty, end ="")
        print(empty) 
show_tree()
show_tree()
show_tree()


 
    # developer fundamentals
    #clean
    # readability
    # predictability 
    #DRy 