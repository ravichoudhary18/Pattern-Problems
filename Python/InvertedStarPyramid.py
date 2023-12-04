def InvertedStarPyramid(number):
    """
    Inverted Star Pyramid
    """
    print('Inverted Star Pyramid')
    space = 0 + 1

    for i in range(number, 0, -1):

        for j in range(space):
            print(end=" ")
        
        for j in range(i):
            print("* ", end=" ")

        space = space + 1
        
        print('\r')

InvertedStarPyramid(5)