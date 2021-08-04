"""Func"""

def func():
    """Mista"""
    text = input().lower()
    tofind = input().lower()

    if text.find("4") > -1 or text.find("four") > -1 or len(text)%4 == 0:
        print("It's not safe four Mista....")
    else:
        if text.count(tofind) > 4:
            print("It's not safe four Mista....")
        else:
            print("MISTA, THIS ONE'S 4 U.")
func()
