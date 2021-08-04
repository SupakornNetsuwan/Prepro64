"""Func"""

def func():
    """Wendy"""
    otheringredient = False
    buncheck = ""
    i = 0
    while True:
        ingredient = input()
        i += 1
        if ingredient == "Vegetables":
            print("We have to cancel your order! Get out!!")
            break
        elif ingredient == "Cheese" or ingredient == "Egg" or ingredient == "Ketchup" or \
        ingredient == "Mayonnaise" or ingredient == "Beef steak" or\
        ingredient == "Chicken steak" or ingredient == "Fish steak" or ingredient == "Bacon" or\
        ingredient == "Sausage" or ingredient == "French fries" or ingredient == "Bun":
            if ingredient == "Bun":
                buncheck += "Bun%d" %i
        elif ingredient != "End":
            otheringredient = True
        elif ingredient == "End": #n-1
            if otheringredient:
                print("I'm not sure if it is a Windy Burger.")
            else:
                lastbun = "Bun%d" %(i-1)
                if buncheck.find("Bun1") == 0 and (lastbun in buncheck) and len(buncheck) > 4:
                    print("This is your burger, have a good meal.")
                else:
                    print("I'm not sure if it is a Windy Burger.")
            break
func()
