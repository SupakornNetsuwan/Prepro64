"""Func"""

def func():
    """Prime number"""
    number = int(input())
    isnotprime = False
    if number in [2, 3]:
        isnotprime = False
    elif number == 1:
        isnotprime = True
    else:
        for i in range(2, number):
            if number%i == 0:
                isnotprime = True
                break
    if isnotprime:
        print("%d is not prime number" %number)
    else:
        print("%d is prime number" %number)
func()

