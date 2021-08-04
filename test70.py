"""Func"""

def func():
    """Call center"""
    price = int(input())
    minutes = int(input())
    second = int(input())

    if price == 0:
        print("free")
    else:
        if second > 30:
            minutes += 1
            second = 0

        if minutes*60 <= 120:
            print("free")
        else:
            if minutes <= 15:
                print(15 * price)
            else:
                print(minutes * price)
func()
