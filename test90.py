"""Func"""

def func():
    """The world"""
    myplacex = int(input())
    myplacey = int(input())
    enemies = int(input())
    enemieshit = 0
    for i in range(0, enemies):
        i = i
        for j in range(1):
            j = j
            distx = int(input())
            disty = int(input())
            if ((myplacex-distx)**2 + (myplacey-disty)**2)**0.5 <= 500:
                enemieshit += 1
    if enemieshit == 1:
        print("You got 1 enemy in your area.")
    elif enemieshit >= 2:
        print("You got %d enemies in your area." %enemieshit)
    else:
        print("Muda Muda Muda.")
func()
