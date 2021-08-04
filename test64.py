"""Func"""

def chk1(num1, num2):
    """2 numbers"""
    return ((num1+num2)+abs(num1-num2))/2
def check2(num1, num2, num3, num4):
    """4 numbers"""
    return ((chk1(num1, num2)+chk1(num3, num4))+abs(chk1(num1, num2)-chk1(num3, num4)))/2

def oneeight():
    """1 - 8"""
    inp1 = float(input())
    inp2 = float(input())
    inp3 = float(input())
    inp4 = float(input())
    inp5 = float(input())
    inp6 = float(input())
    inp7 = float(input())
    inp8 = float(input())
    return chk1(check2(inp1, inp2, inp3, inp4), check2(inp5, inp6, inp7, inp8))

def ninefifteen():
    """9 - 15"""
    inp9 = float(input())
    inp10 = float(input())
    inp11 = float(input())
    inp12 = float(input())
    inp13 = float(input())
    inp14 = float(input())
    inp15 = float(input())
    return chk1(check2(inp9, inp10, inp11, inp12), chk1(chk1(inp13, inp14), inp15))

def func():
    """Just max it"""
    print("%.2f" %chk1(oneeight(), ninefifteen()))
func()
