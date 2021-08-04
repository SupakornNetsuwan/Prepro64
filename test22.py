"""Func"""

def pos():
    """max"""
    height1 = float(input())
    height2 = float(input())
    height3 = float(input())
    height4 = float(input())
    height5 = float(input())
    height6 = float(input())

    print("max : %.2f" %(max((height1, height2, height3, height4, height5, height6))))
    print("min : %.2f" %(min((height1, height2, height3, height4, height5, height6))))
    print("sum : %.2f" %(sum((height1, height2, height3, height4, height5, height6))))
    print("avg : %.4f" %(sum((height1, height2, height3, height4, height5, height6))/6))

pos()
