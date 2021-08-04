"""Func"""

def main():
    """Temp"""
    celsius = float(input())
    print("Celsius    = %.4f" %celsius)
    print("Fahrenheit = %.4f" %((celsius * 9)/5+32))
    print("Kelvin     = %.4f" %(celsius + 273.15))
    print("Rankine    = %.4f" %((celsius + 273.15) * (9/5)))
    print("Reaumer    = %.4f" %(celsius * (4/5)))
main()
