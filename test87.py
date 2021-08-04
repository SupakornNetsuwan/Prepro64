"""Func"""

def func():
    """Multiply"""
    print("-------------")
    for i in range(2, 13):
        for j in range(1, 13):
            print("%2s x %2s = %3s" %(i, j, i*j))
        print("-------------")
func()
