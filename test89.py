"""Func"""

def func():
    """Alphabet counter"""
    text = input()
    upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    number = "1234567890"
    upcasestack = 0
    lowcasestack = 0
    numstack = 0
    for alphabet in text:
        if alphabet in upcase:
            upcasestack += 1
        elif alphabet in lowcase:
            lowcasestack += 1
        elif alphabet in number:
            numstack += 1
    print("%d number(s)" %numstack)
    print("%d uppercase letter(s)" %upcasestack)
    print("%d lowercase letter(s)" %lowcasestack)
func()
