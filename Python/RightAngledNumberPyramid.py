def RightAngledNumberPyramid(number):
    for i in range(1,number+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print('\n')

RightAngledNumberPyramid(4)