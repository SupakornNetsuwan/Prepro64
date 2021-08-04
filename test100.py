"""Func"""

def func():
    """Stair"""
    steps = int(input())
    for i in range(1, steps+1):
        stackers = ""
        for j in range(1, i+1):
            stackers += "%d" %j
        for j in range(i-1, 0, -1):
            stackers += "%d" %j
        print(stackers)
func()
