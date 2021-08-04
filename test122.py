"""Func"""

def ordercheck(order):
    """Order check"""
    cost = 0
    if order == "Wash The Hair":
        cost = 120
    elif order == "Wash-Cut-Dry":
        cost = 170
    elif order == "Haircut":
        cost = 50
    elif order == "Perm":
        cost = 300
    elif order == "Snip":
        cost = 350
    elif order == "Hair Straightening":
        cost = 250
    elif order == "Hair Dye":
        cost = 400
    elif order == "Eyebrow Tattoo":
        cost = 700
    elif order == "Lip Tattoo":
        cost = 800
    elif order == "Make Up":
        cost = 1000
    return cost

def func():
    """Salon"""
    name = input()
    nationality = input().capitalize()
    discount = 0

    if input() and input() == "Y":
        discount = int(input())

    totalorder = []
    totalcost = 0 - discount
    for _ in range(3):
        order = input()
        cost = ordercheck(order)
        if order != "-":
            totalorder.append(order)
            totalcost += cost * (((nationality == "Malaysian") * 2) + \
            (nationality != "Malaysian" * 1))

    mylist = []
    for order in totalorder:
        if order + " " + str(totalorder.count(order)) not in mylist:
            mylist.append(order + " " +str(totalorder.count(order)))

    if totalcost < 0:
        totalcost = 0

    for order in mylist:
        print(order)
    print(name, totalcost, "Baht")
func()
