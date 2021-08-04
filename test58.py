"""Func"""

def func():
    """Grade checker"""
    def checker(point):
        """checker"""
        if point >= 80:
            print("A")
        elif point < 80 and point >= 75:
            print("B+")
        elif point < 75 and point >= 70:
            print("B")
        elif point < 70 and point >= 65:
            print("C+")
        elif point < 65 and point >= 60:
            print("C")
        elif point < 60 and point >= 55:
            print("D+")
        elif point < 55 and point >= 50:
            print("D")
        else:
            print("F")

    checker(float(input()))
func()
