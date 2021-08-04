"""Func"""

def func():
    """Just max it"""
    numbers = []
    for _ in range(int(input())):
        numbers.append(float(input()))
    numbers.sort()
    print("%.2f" %numbers[-1])
func()
