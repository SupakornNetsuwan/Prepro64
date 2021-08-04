"""Func"""

def func():
    """Sort"""
    mylist = []
    while True:
        message = input().capitalize()
        if message == "Stop":
            break
        elif message.isalpha():
            mylist.append(message)
    mylist.sort()
    for mem in mylist:
        print(mem)
func()
