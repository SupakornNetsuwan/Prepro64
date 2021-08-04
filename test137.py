"""Func"""

def func():
    """All for prime"""
    start = int(input())
    stop = int(input())
    sumprime = 0
    answer = ""
    for number in range(start, stop+1):
        isprime = True
        if number == 1:
            isprime = False
        elif number in [2, 3]:
            isprime = True
        else:
            for i in range(2, number):
                if number % i == 0:
                    isprime = False
                    break
        if isprime:
            answer += str(number) + " "
            sumprime += number
    if answer:
        print(answer)
        print("sum of prime =", sumprime)
    else:
        print("not found prime number")
func()
