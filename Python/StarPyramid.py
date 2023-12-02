def StarPyramid(number):
    """
    Star Pyramid
    """
    print('Star Pyramid')
    for i in range(number+1):
        for j in range(number):
            print(" ", end= "")
        
        for k in range(i):
            print("* ", end= "")
        print()

StarPyramid(5)