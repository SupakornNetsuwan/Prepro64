"""Func"""

def qubitmanage(order, qubit):
    """Qubit manage"""
    if order == "INC":
        return qubit + 1
    elif order == "DEC":
        return qubit - 1
    elif order == "DUBL":
        return qubit * 2
    elif order == "HALF":
        return qubit / 2

def func():
    """Quantum cpmputer"""
    boot, frz, qubit, count = False, False, 0, 0
    while True:
        order = input().upper()
        count += 1

        if count <= 1000 or frz:
            if order == "FRZ":
                frz = True
            elif order == "BOOT":
                boot = True
            elif order in "INC DEC DUBL HALF":
                qubit = qubitmanage(order, qubit)
            elif order == "END":
                if not boot:
                    print("WARN: MissingBootInstruction (QCP003)\n0.000000")
                    break
                elif boot and not frz and count <= 1000:
                    print("WARN: AbsoluteZero (QCP001)\n%.6f" %qubit)
                    break
                else:
                    print("%.6f" %qubit)
                    break
        else:
            print("ERROR: NonAbsoluteZeroLimitExceeded (QCP002)\n%.6f" %qubit)
            break
func()