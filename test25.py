"""Func"""
import math

def func():
    """clock"""
    length = float(input())
    freq = "%.2f Hz" %((1/(math.pi*2))*(math.sqrt(9.81/length)))
    print(freq)
func()
