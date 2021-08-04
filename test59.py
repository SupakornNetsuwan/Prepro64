"""Func"""

def func():
    """How to travel"""
    weather = input()
    imortance = input()
    rane = float(input())

    def traveling(rane):
        """Finding way"""
        if rane >= 300:
            print("Private jet")
        elif rane < 300 and rane >= 20:
            print("Car")
        elif rane < 20 and rane >= 1:
            print("Motorcycle")
        else:
            print("Walk")

    if rane < 0:
        print("Error")
    else:
        if weather == "sunny":
            traveling(rane)
        elif weather == "rainy" and imortance == "important":
            traveling(rane)
        else:
            print("Not go")
func()
