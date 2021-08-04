"""Func"""

def caesar():
    """caesar"""
    alpha = input()
    pos = ord(alpha) + 5
    print(chr(((pos//91) * 64) + (pos - (90 * (pos//91)))))
caesar()
