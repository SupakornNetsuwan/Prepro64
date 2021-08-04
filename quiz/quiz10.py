"""Func"""

def findsmalleft(row, col):
    lowest = []
    for i in range(min([row+1, col+1])):
        lowest = [col-i, row-i]
    return lowest
def func():
    """Func"""
    row, col = int(input()), int(input())
    smallxy = findsmalleft(row, col)
    print(smallxy)
    for y in range(-1,8):
        for x in range(8):
            if y == -1:
                print(" _", end="")
            elif x == smallxy[0] + x and y == smallxy[1] + x and (y != row and x!= col):
                # print((x, y), end="")
                print("|x", end="")
            else:
                if y == row or x == col:
                    if y == row and x== col:
                        print("|Q", end="")
                    else:
                        print("|x", end="")
                else:
                    print("|_", end="")
        if y != -1:
            print("|", end="")
        print()
func()