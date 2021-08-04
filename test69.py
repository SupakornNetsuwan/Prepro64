"""Func"""

def func():
    """Noodle"""
    brand = input().lower()
    taste = input()
    pack = int(input())

    def noodlefind(noodle):
        """Pork or not"""
        if taste.lower().find("pork") > -1:
            print(int(noodle))
        else:
            print(int(noodle*1.1))

    if brand == "chotipat":
        noodlefind(280 * pack)
    elif brand == "mawai":
        noodlefind(238 * pack)
    elif brand == "nisjung":
        noodlefind((280 + (35**0.5)*3) * pack)
    elif brand == "yummayro":
        noodlefind(275 * pack)
    else:
        print("No Data !!")

func()
