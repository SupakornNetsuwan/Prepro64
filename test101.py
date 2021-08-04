"""Func"""

def func():
    """Pyramid"""
    stacker = ""
    level = int(input())
    for i in range(1, level+1):
        space = level - i
        stacker += space*" "
        for j in range(i*2-1):
            j = j
            stacker += "*"
        stacker += "\n"
    for i in range(level-1, 0, -1):
        alllength = (level)*2-1
        stacker += " " * ((alllength - (2*i-1))//2)
        stacker += "*" * (2*i-1)
        if i != 1:
            stacker += "\n"
    print(stacker)
func()
