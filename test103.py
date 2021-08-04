"""func"""

def func():
    """Diamond"""
    numbers = int(input())
    stacker = ""
    for i in range(numbers):
        # space ซ้าย
        space = (6*(numbers-1)+1)//2 - i*3
        stacker += space * " "
        # ตัวเลขซ้าย
        for j in range(i+1, 0, -1):
            stacker += "%d " %j
        #space ตรงกลาง
        for j in range(i*2-2):
            stacker += " "
        #ตัวเลขขวา
        for j in range(1, i+2):
            if i != 0:
                stacker += "%d " %j
        stacker += "\n"
    for i in range(1, numbers): # 1 2 3 4 5
        # space ซ้าย
        stacker += " "*(i*3)
        # ตัวเลขซ้าย
        for j in range(numbers - i, 0, -1):
            stacker += "%d " %j
        # space ตรงกลาง
        for j in range((numbers-i-2)*2):
            stacker += " "
        # ตัวเลขขวา
        for j in range(1, numbers - i+1):
            if i != numbers - 1:
                stacker += "%d " %j
        if i != numbers-1:
            stacker += "\n"
    print(stacker)
func()
