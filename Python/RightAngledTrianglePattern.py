def RightAngledTrianglePattern(number):
    for i in range(number):
        print("*", end=' ')
        for j in range(i):
            print("*", end=' ')
        print('\n')

RightAngledTrianglePattern(4)