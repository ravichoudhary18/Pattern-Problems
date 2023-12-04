from icecream import ic

def DiamondStarPattern(number):
    """
    Diamond Star Pattern
    """
    print("Diamond Star Pattern")
    number = number + 1
    upper_space = number - 1 
    lower_space = 1

    for i in range(number):
        for j in range(upper_space):
            print(end=" ")
        for j in range(i):
            print("*", end=" ")
        upper_space = upper_space - 1
        print("\r")

    number = number-2
    for i in range(number, 0, -1):
        for j in range(lower_space):
            print(end=" ")
        for j in range(i):
            print("*", end=" ")
        lower_space = lower_space + 1
        print("\r")

DiamondStarPattern(5)