def InvertedRightPyramid(number):
    """
    Inverted Right Pyramid
    """
    print("Inverted Right Pyramid")
    for i in range(number):
        for j in range(number - i):
            print("*", end=' ')
        print('\r')

InvertedRightPyramid(5)