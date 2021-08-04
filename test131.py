"""Func"""

def func():
    """#2"""
    numbers = list(map(float, input().split(" ")))
    lookfor = float(input())
    findnum = [i for i, x in enumerate(numbers) if x == lookfor]
    if findnum:
        print("Index: %d" %findnum[-1])
    else:
        findnum2 = [abs(lookfor - i) for i in numbers]
        print("Index:", findnum2.index(min(findnum2)))
        print("Number: %.2f" %numbers[findnum2.index(min(findnum2))])
func()
