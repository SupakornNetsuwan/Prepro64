"""Func"""

def findnum():
    """Find num"""
    input1 = float(input())
    input2 = float(input())
    print("%.3f" %(sum((input1, input2)) - min(input1, input2)))
findnum()
