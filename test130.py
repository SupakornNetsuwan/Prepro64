"""Func"""

def func():
    """#1"""
    numbers = list(map(int, input().split(" ")))
    leng = int(input())
    if leng > len(numbers):
        leng = len(numbers)
    maxnum, pair1 = float('-inf'), []
    for i in range(len(numbers)-leng+1):
        stacker, pair2 = 0, []
        for j in range(leng):
            stacker += numbers[i+j]
            pair2.append(numbers[i+j])
        if stacker >= maxnum:
            maxnum = stacker
            pair1 = pair2
    print(pair1)
    print(maxnum)
func()
