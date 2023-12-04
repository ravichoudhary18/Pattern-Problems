def StarPyramid(number):
    """
    Star Pyramid
    """
    print('Star Pyramid')
    space = number -1
    for i in range(number):
        
        for j in range(space):
            print(end=" ")

        for j in range(i+1):
            print("* ", end=" ")

        space = space - 1
        print('\r')

StarPyramid(5)