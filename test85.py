"""Func"""

def func():
    """series"""
    start = int(input())
    end = int(input())
    diff = int(input())

    if end < start and start != end:
        end -= 1
    elif end > start and start != end:
        end += 1
    for i in range(start, end, diff):
        print(i)
func()
