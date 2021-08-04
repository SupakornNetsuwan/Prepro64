"""Func"""

def func():
    """burger"""
    inputtext = input()
    breads_amount = len(inputtext)%10
    pieces_burger = inputtext.lower().find("burger")
    burger = ""

    for i in range(1, (breads_amount+1)):
        i = i
        burger += "(|"
    for i in range(1, (pieces_burger+1)):
        i = i
        burger += "{}"
        i = i
    for i in range(1, (breads_amount+1)):
        burger += "|)"
    # burger += "(|" * breads_amount
    # burger += "{}" * pieces_burger
    # burger += "|)" * breads_amount
    print(burger)
func()
