"""Func"""

def func():
    """Dota2 kebab"""
    price = int(input())
    amount = int(input())
    feedb = input()
    if feedb == "This kebab is very good":
        print("%.2f" %((0.7*price) * amount))
    elif feedb == "This is not good not bad":
        print("%.2f" %((0.95*price) * amount))
    elif feedb == "This is not kebab":
        print("%.2f" %((1.16*price) * amount))
    else:
        print("%.2f" %0)
func()
