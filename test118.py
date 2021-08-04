"""Func"""

def func():
    """Multiply"""
    times = int(input())
    mylist = []
    for _ in range(times):
        mylist.append(int(input()))
    multiply = float(input())
    print(list(map(lambda n: "%.2f" %(n*multiply), mylist)))
func()
