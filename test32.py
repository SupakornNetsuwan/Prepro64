"""Func"""

def func():
    """Electric sign"""
    message = input().upper()
    length = len(message) + 4
    print("|%s|" %(length * "-"))
    print("|  %s  |" %message)
    print("|%s|" %(length * "-"))
func()
