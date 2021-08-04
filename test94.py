"""Func"""

def func():
    """Doctor riding a motorcycle"""
    signal = input()
    spliter = len(max(signal.split("0")))
    if spliter < 1:
        spliter = 1
    elif spliter >= 6:
        spliter = 6
    checker = ["Rank D", "Rank C", "Rank B", "Rank A", "Rank S", "Rank SSS"]
    print(checker[spliter-1])
func()
