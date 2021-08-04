"""Func"""

def func():
    """Vending machine"""
    total = 0
    counter = 0
    while True:
        action = input()
        if action == "END":
            break
        elif action[0] != "-":
            total += int(action)
        else:
            if total >= int(action[1:]):
                total -= int(action[1:])
                counter += 1
            else:
                print("ERROR: Not enough money for this item.")
    print("Items: %d" %counter)
    print("Change: %d THB" %total)
func()
