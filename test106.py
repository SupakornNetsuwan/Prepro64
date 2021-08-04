"""Func"""

def func():
    """Letter"""
    password = ""
    rows = int(input())
    for _ in range(rows):
        text = input()
        for alphabet in text:
            if alphabet.isalpha():
                password += alphabet
    print(password)
func()
