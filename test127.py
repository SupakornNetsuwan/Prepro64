"""Func"""

def func():
    """Football"""
    pain = input().lower()
    if pain == "y":
        print("you will unavaliable")
    else:
        late = input().lower()
        if late != "y":
            print("you will be a starter")
        else:
            prac = input().lower()
            if prac == "y":
                print("you will be a substitute")
            else:
                print("you won't be selected")
func()
