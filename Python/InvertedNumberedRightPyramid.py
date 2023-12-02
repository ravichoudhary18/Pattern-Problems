def InvertedNumberedRightPyramid(number):
    """
    Inverted Numbered Right Pyramid
    """
    print("Inverted Numbered Right Pyramid")
    for i in range(1, number+1):
        for j in range(1, number+1 - i):
            print(j, end=' ')
        print('\r')

InvertedNumberedRightPyramid(5)