"""Func"""

def trick1(pos):
    "Trick 1"
    newpos1 = pos.pop(0)
    newpos2 = pos.pop(0)
    newpos3 = pos.pop(0)
    return list((newpos2, newpos1, newpos3))

def trick2(pos):
    "Trick 2"
    newpos1 = pos.pop(0)
    newpos2 = pos.pop(0)
    newpos3 = pos.pop(0)
    return list((newpos1, newpos3, newpos2))

def trick3(pos):
    "Trick 3"
    newpos1 = pos.pop(0)
    newpos2 = pos.pop(0)
    newpos3 = pos.pop(0)
    return list((newpos3, newpos2, newpos1))

def findposition(firstpos, position):
    """Find last position"""
    arr1 = position.pop(0)
    arr2 = position.pop(0)
    if firstpos == arr1:
        return "A"
    elif firstpos == arr2:
        return "B"
    else:
        return "C"

def func():
    """Main func"""
    firstpos = input()
    position = list(("A", "B", "C"))
    count = 0
    while True:
        trickmove = input()
        count += 1
        if trickmove == "1":
            position = trick1(position)
        elif trickmove == "2":
            position = trick2(position)
        elif trickmove == "3":
            position = trick3(position)
        elif trickmove == "stop":
            print("ball in cup", findposition(firstpos, position))
            print("shuffle", count-1, "time")
            break
func()
