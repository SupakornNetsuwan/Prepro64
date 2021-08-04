"""Func"""

def func():
    """escape string"""
    input1 = input()
    input2 = input()
    input3 = input()

    print("%s\t%s\t%s" %(input1, input2, input3))
    print("%s\t%s\t%s" %(input3, input1, input2))
    print("%s\t%s\t%s" %(input2, input3, input1))
func()
