"""Func"""

def func():
    """Just max it"""
    malist = []
    for _ in range(int(input())):
        malist.append(float(input()))
    print("%.2f" %(max(malist)))
func()
