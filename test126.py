"""Func"""

def answer(stacker, err):
    """answer"""
    for ing in err:
        print(ing)
    print("Your order will be..")
    for ing in stacker:
        print(ing)

    if "Vegetables" not in stacker and stacker[0] == "Bun" and stacker[-1] == "Bun"\
        and len(stacker) >= 3:
        print("Result: This is how it should be done!!")
    else:
        print("Result: That one is the worst.")

def func():
    """Wendys' burger V.2"""
    stacker = []
    err = []
    while True:
        order = input()
        ingredient = ["Cheese", "Egg", "Ketchup", "Mayonnaise", "Beefsteak", "Chicken steak",\
            "Fish steak", "Bacon", "Sausage", "French fries", "Bun", "Vegetables"]
        if order == "OK":
            break
        if order[0] == "+" and order[1:] in ingredient:
            stacker.append(order[1:])
        elif order[0] == "+" and order[1:] not in ingredient:
            err.append("We don't have '%s', sir." %order[1:])
        elif order[0] == "-" and order[1:] in stacker:
            for _ in range(stacker.count(order[1:])):
                stacker.remove(order[1:])
        elif order[0] == "-" and order[1:] not in stacker:
            err.append("There are no '%s' in your order, sir." %order[1:])
        elif order[0:2].isdigit() and order[2:] in ingredient:
            stacker.insert(int(order[0:2]), order[2:])
        elif order[0:2].isdigit() and order[2:] not in ingredient:
            err.append("We don't have '%s', sir." %order[2:])
        else:
            err.append("I beg your pardon?")
    answer(stacker, err)
func()
