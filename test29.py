"""Func"""

def func():
    """bank note"""
    inputtext = int(input())
    thoundsand = inputtext//1000 #1
    fivehundred = (inputtext - (thoundsand*1000))//500 #1
    hundred = (inputtext-((fivehundred*500) + (thoundsand*1000)))//100
    ffty = (inputtext-((hundred*100) + (fivehundred*500) + (thoundsand*1000)))//50
    twenty = (inputtext-((ffty*50) + (hundred*100) + (fivehundred*500) + (thoundsand*1000)))//20

    print("%d\n%d\n%d\n%d\n%d\n" %(thoundsand, fivehundred, hundred, ffty, twenty))
func()
