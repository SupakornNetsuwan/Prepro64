"""Func"""

def func():
    """Orange cake"""
    cash = int(input())
    price = int(input())
    if cash > price:
        print("Orange Cake:", cash//price)
        print("Money left:", cash%price)
    else:
        print("Not enough money;(\nMoney left:", cash)
func()
