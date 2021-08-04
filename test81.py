"""Func"""

def func():
    """Catching jerry"""
    polices = int(input())
    trapdefend = False

    while True:
        action = input()
        if action == "The trap is set.":
            trapdefend = True
        elif action == "No trap here":
            trapdefend = False
        elif action == "Boom!!!":
            if not trapdefend:
                polices -= 1
                trapdefend = True
        if polices == 0:
            print("Gokaijerry is alive.")
            break
        elif action == "Catch the Gokaijerry":
            print(polices, "police is catching Gokaijerry.")
            break
func()
