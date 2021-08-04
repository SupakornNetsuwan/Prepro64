"""Func"""

def func():
    "Steps"
    steps = int(input())
    for i in range(1, steps+1):
        stacker = ""
        for j in range(i):
            j = j
            stacker += "%d" %i
        print(stacker)
func()
