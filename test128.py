"""Func"""

def func():
    """Balls"""
    ball1, ball2, ball3 = input(), input(), input()
    if ball1 == ball2 == ball3 == "RED":
        print("GiftVoucher")
    elif ball1 == ball2 == ball3 == "BLUE":
        print("DoraemonDoll")
    elif ball1 == ball2 == ball3 == "GREEN":
        print("FruitBasketBoxset")
    elif ball1 == ball2 == ball3 == "GOLD":
        print("NintendoSwitch")
    elif ball1 != ball2 != ball3:
        print("TissueBox")
    else:
        print("NoodleCups")
func()
