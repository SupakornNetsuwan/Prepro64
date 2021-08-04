"""Func"""

def func():
    """go pro dota"""
    age = int(input())

    if age >= 17 and age <= 23:
        if age < 20:
            permission = input()
            if permission == "Y":
                experience = int(input())
                travel = input()
                if experience >= 12 and travel == "Y":
                    print("You can be in OG!")
                else:
                    print("May be next time.")
            else:
                print("May be next time.")
        else:
            experience = int(input())
            travel = input()
            if experience >= 12 and travel == "Y":
                print("You can be in OG!")
            else:
                print("May be next time.")
    else:
        print("May be next time.")
func()
