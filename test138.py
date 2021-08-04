"""Func"""

def primecheck(number):
    """Prime checker"""
    if number != 1:
        for i in range(2, number):
            if number%i == 0:
                break
        else:
            return True

def func():
    """Func"""
    code = input()
    codesplit = [code[i: i+3] for i in range(0, len(code), 3)]
    codemap = sum(list(map(lambda n: int(n)**2, codesplit)))
    answer = False
    for number in range(codemap, 0, -1): # 4 3 2 1
        if number in [2, 3]:
            answer = number
            break
        else:
            if primecheck(number):
                answer = number
                break
    if answer:
        print("BASE NO.%s" %answer)
    else:
        print("Optimus not found")
func()
