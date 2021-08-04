"""Func prepro"""
import math

def func():
    """sandwich"""
    inputa = float(input())
    inputb = float(input())
    deg = math.atan(inputa/inputb)
    print("%.2f deg" %(math.degrees(deg)))
func()
