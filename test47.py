"""Func"""

def func():
    """Club check"""
    amount = float(input())
    print(("Welcome!" * (amount > 0)) or ("Get out!" * (amount <= 0)))
func()
