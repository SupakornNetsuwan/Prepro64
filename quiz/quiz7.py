"""Func"""

def func():
    """The screen"""
    width = int(input())
    height = int(input())
    justi = input()
    linedis = int(input())
    messsage = input()
    line = ""
    for width in range(width):
        line += "-"
    newmess = ""
    for i in range(width - len(messsage)):
        if justi == "1":
            if i == width - len(messsage) - 1:
                newmess += messsage
            else:
                newmess += " "
        else:
            if i == 0:
                newmess += messsage
            else:
                newmess += " "
    print(line)
    for height in range(height-2):
        if linedis-1 != height:
            print("|", end="")
            print(" " * (width-1), end="")
            print("|", end="")
        else:
            print("|", end="")
            print(newmess, end="")
            print("|", end="")
        print()
    print(line)
func()
