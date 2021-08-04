"""Func"""

def func():
    """Battery"""
    batt = int(input())
    length = int(input())
    ava = (batt/100)*length

    battdis = (int(ava)*"O")
    totaldis = (length-int(ava))*"_"
    print("(%s%s) %s" %(battdis, totaldis, (str(batt)+"%")))
func()
