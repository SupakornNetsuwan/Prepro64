"""Func"""
import math

def func():
    """fog func"""
    number = float(input())
    def gxfunc(number):
        """g(x)"""
        return math.pow(number, 3) + (4*number) - 1
    def fxfunc(number):
        """f(x)"""
        return (15 + number - (math.pow(number, 3)))/((math.pow(number, 2)/3)+11)

    print("%.4f" %float(fxfunc(gxfunc(number))))
    print("%.4f" %float(gxfunc(fxfunc(number))))
func()
