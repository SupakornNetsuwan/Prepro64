"""Func"""

def func():
    """Multiply"""
    number = int(input())
    print("-----------------")
    for i in range(1, 13):
        print("%3s x%4s =%6s" %(number, i, number*i))
    print("-----------------")
func()
