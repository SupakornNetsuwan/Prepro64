"""Heart count"""

def heart():
    """Health"""
    available = int(input())
    bonus = int(input())
    allheart = (available * "<3") + (bonus  * "<3")
    space = 10 - (available + bonus)
    total = allheart + (space * "_")

    print("My Heart %d Heart |%s|" %(available, total))
    print("My Bonus %d Heart" %bonus)
heart()
