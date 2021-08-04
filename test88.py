"""Func"""

def func():
    """Quantum computer"""
    times = int(input())
    qubit = 0
    count = 0
    while count < times:
        count += 1
        order = input().upper()
        if order == "INC":
            qubit += 1
        elif order == "DEC":
            qubit -= 1
        elif order == "DUBL":
            qubit *= 2
        elif order == "HALF":
            qubit /= 2
    print("%.2f" %qubit)
func()
