"""Func"""

def func():
    """Append"""
    listname = ""
    times = int(input())
    for _ in range(times):
        alpha = input()
        listname += alpha + " "
    print(listname)
func()
