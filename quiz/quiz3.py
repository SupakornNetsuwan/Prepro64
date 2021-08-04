"""Func"""

def func():
    """L"""
    number = input()
    print("%.5d" %int(str((sum([int(i) for i in number])**3 + int(number[0:5])))[0:5]))
func()
