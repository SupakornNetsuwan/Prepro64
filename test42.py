"""Func prepro"""

def func():
    """digit"""
    number = input()
    zero = number.count("0")
    one = number.count("1")
    two = number.count("2")
    three = number.count("3")
    four = number.count("4")
    five = number.count("5")
    six = number.count("6")
    seven = number.count("7")
    eight = number.count("8")
    nine = number.count("9")
    print(zero + one + two + three + four + five + six + seven + eight + nine)
func()
