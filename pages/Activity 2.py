
import numpy as np
import matplotlib.pyplot as plt

"""
Flood Fill Algorithm Replaces the Old Value into the New Value if it has the Same values as defined by the Initial Color
Algorithm:
    if(twoD_array[row][column] == old_value)
        twoD_array[row][column] = new_value

Members:
    Billena, Dhominick John
    Torre, Jephone Israel Jireh
    Artacho, Cristopher Ian
"""

twoD_array = np.array([     [1, 1, 1, 1],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]])


def floodFillChecker(oldColor, newColor):
    # Size of the Shape to Fill
    X = 4
    Y = 4 

    for i in range(len(twoD_array)):
        for row in range(len(twoD_array)):
            for column in range(len(twoD_array)):
                checkColor = twoD_array[row][column]
                if(checkColor == oldColor):
                    twoD_array[row][column] = newColor
                    # print(twoD_array)

def main():
    print(twoD_array)
    oldColor = int(input("What is the Old Color to Change (0 | White & 1 | Black): "))
    newColor = int(input("What is the Replacement Color (0 | White & 1 | Black): "))
    floodFillChecker(oldColor, newColor)
    print(twoD_array)
    plt.imshow(twoD_array, interpolation = 'none', cmap = 'gray_r')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()