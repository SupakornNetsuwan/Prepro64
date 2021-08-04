"""Func"""

def func():
    """X"""
    number = input()
    for i in range(len(number)): # 0 1 2 3
        for j in range(len(number)): # 0 1 2 3
            if j == i:
                print("%s" %number[j], end=" ")
            elif j + i == len(number)-1:
                print("%s" %number[j], end=" ")
            else:
                print(" ", end=" ")
        print()
func()
