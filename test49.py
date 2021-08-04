"""Func"""

def func():
    """sum"""
    input1 = int(input())
    input2 = int(input())
    input3 = int(input())
    if (input1+input2+input3)/3 == input1:
        print(0)
    else:
        if input1 == input3:
            input1 = 0
            input3 = 0
        elif input1 == input2:
            input1 = 0
            input2 = 0
        if input2 == input3:
            input2 = 0
            input3 = 0
        print(input1+input2+input3)
func()
