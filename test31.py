"""Func"""

def func():
    """Digit count"""
    input1 = int(input().replace(",", "").replace("-", ""))
    print(len(str(input1)))

func()
