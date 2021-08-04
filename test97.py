"""Func"""

def func():
    """Password hack"""
    passlength = int(input())
    correctpass = ""
    passstacker = ""
    for i in range(passlength):
        i = i
        correctpass += input()
    while True:
        passstacker += input()
        if correctpass in passstacker:
            print("Finally, We found this treasure.")
            print(len(passstacker))
            break
func()
