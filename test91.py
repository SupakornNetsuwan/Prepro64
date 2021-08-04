"""Func"""

def func():
    """Sexy"""
    flick = int(input())
    arrs1 = []
    arrs2 = []
    for i in range(flick*2):
        action = int(input())
        if i%2 == 0:
            arrs1.append(action)
        else:
            arrs2.append(action)
    stacker = 0
    total = 0
    for i in range(len(arrs1)):
        if arrs1[i] == arrs2[i]:
            stacker += 1
            total += stacker
        else:
            stacker = 0
            total -= 1
    print(total, "Point")
func()
