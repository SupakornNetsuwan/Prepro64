"""Func"""

def func():
    """Grade"""
    points = int(input())
    zero = float(0)*(points < 50)
    one = float(1)*(points < 55 and points >= 50)
    onehalf = float(1.5)*(points < 60 and points >= 55)
    two = float(2)*(points < 65 and points >= 60)
    twohalf = float(2.5)*(points < 70 and points >= 65)
    three = float(3)*(points < 75 and points >= 70)
    threehalf = float(3.5)*(points < 80 and points >= 75)
    four = float(4)*(points <= 100 and points >= 80)
    print(sum((zero, one, onehalf, two, twohalf, three, threehalf, four)))
func()
