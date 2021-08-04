"""Func"""

def func(number, maxnum=float("inf")):
    """#4"""
    for i in range(len(number)-1):
        if abs(number[i]-number[i+1]) <= maxnum:
            maxnum = abs(number[i]-number[i+1])
    print(maxnum)
func(list(map(int, input().split(" "))))
