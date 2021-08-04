"""Func"""

def func():
    """Check end"""
    text = ""
    while True:
        textinput = input().lower()
        if textinput.isalpha() and textinput != "end":
            text += " %s" %textinput
        if textinput == "end":
            print(text.count(input().lower()))
            break
func()
