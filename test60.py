"""Func"""

def func():
    """Finding type"""
    symbol = "%.1s" %input()
    alphabet = "abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "1234567890"

    if alphabet.find(symbol)+1 and number.find(symbol)+1 == False:
        print("'%s' is an alphabet." %symbol)
    elif number.find(symbol)+1 and alphabet.find(symbol)+1 == False:
        print("'%s' is numeric." %symbol)
    else:
        print("'%s' is not both an alphabet and numeric." %symbol)
func()
