"""Func"""

def checkprime(number):
    """Check for prime"""
    if number <= 3:
        return False if number == 1 else True
    if number%2 == 0 or number%3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6
    return True

def func():
    """Func"""
    number = int(input())
    if checkprime(number):
        print(number, "is prime number")
    else:
        print(number, "is not prime number")
func()
