"""Func"""

def func():
    """Year finding"""
    year = int(input())
    if year%4 == 0 and year%100 != 0:
        print("%d is a leap year." %year)
    elif year%100 == 0 and year%400 == 0:
        print("%d is a leap year." %year)
    else:
        print("%d is not a leap year." %year)
func()
