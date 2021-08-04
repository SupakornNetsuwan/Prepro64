"""Func"""

def func():
    """Icecream"""
    me_x = int(input())
    me_y = int(input())
    icea_x = int(input())
    icea_y = int(input())
    iceb_x = int(input())
    iceb_y = int(input())

    def distance(ice_x, ice_y):
        """Find distance"""
        return (pow(me_x-ice_x, 2) + pow(me_y-ice_y, 2))**0.5

    if distance(icea_x, icea_y) > distance(iceb_x, iceb_y):
        print("B")
    elif distance(icea_x, icea_y) < distance(iceb_x, iceb_y):
        print("A")
    elif distance(icea_x, icea_y) == distance(iceb_x, iceb_y):
        if icea_y > iceb_y:
            print("A")
        elif icea_y < iceb_y:
            print("B")
        else:
            if icea_x < iceb_x:
                print("A")
            elif icea_x > iceb_x:
                print("B")
            else:
                print("A")

func()
