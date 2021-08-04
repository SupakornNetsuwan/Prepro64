"""Func"""

def func():
    """Guess"""
    wantnumber = int(input())
    times = int(input())
    i = 0
    while i < times:
        guess = int(input())
        if guess == wantnumber:
            print("Yes! It is %d." %guess)
            break
        if i == times-1:
            print("No more chances. You lose.")
            break
        i += 1
func()
