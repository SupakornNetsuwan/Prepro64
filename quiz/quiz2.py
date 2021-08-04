"""Func"""

def func():
    """Magic school"""
    name = input()
    age = int(input())
    sex = input()
    height = float(input())

    message = "You can not join this school."
    if 13 <= age <= 15:
        if sex == "Male":
            if height >= 160:
                message = "You can study in junior high school."
        else:
            if height >= 155:
                message = "You can study in junior high school."
    elif 16 <= age <= 18:
        if sex == "Male":
            if height >= 170:
                message = "You can study in senior high school."
        else:
            if height >= 165:
                message = "You can study in senior high school."

    if sex == "Male":
        print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
    else:
        print("Miss %s Age: %d Height: %.2f" %(name, age, height))
    print(message)
func()
