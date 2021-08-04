"""Func"""

def checkprimenumber(number):
    """solve"""
    if number == 1:
        return False
    for numbb in range(2, int(number**0.5)+1):
        if number % numbb == 0:
            break
    else:
        return True

def sumprime(checkprime):
    """Sum prime"""
    count = 0
    if checkprime <= 3:
        onethree = {
            "1":"1 is not prime number",
            "2":"2 is prime number",
            "3":"3 is is super prime number"
        }
        print(onethree[str(checkprime)])
        return
    if checkprime%2 == 0 or checkprime%3 == 0:
        print(checkprime, "is not prime number")
        return

    for i in range(checkprime, 0, -1):
        if checkprimenumber(i):
            count += 1
    if checkprimenumber(count) and checkprimenumber(checkprime):
        print(checkprime, "is super prime number")
    elif checkprimenumber(checkprime):
        print(checkprime, "is prime number")
    else:
        print(checkprime, "is not prime number")

def func():
    """Func"""
    number = int(input())
    sumprime(number)
func()
