"""Func"""

def func():
    """sum"""
    alphab = input()
    arrs = list(("A", "E", "I", "O", "U"))
    if alphab in arrs:
        print(alphab, "is vowel.")
    else:
        print(alphab, "is consonant.")
func()
