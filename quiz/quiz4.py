"""Func"""

def func():
    """Func"""
    money = int(input())
    direc = list(map(int, input().split(" ")))

    hotellist = []
    for _ in range(int(input())):
        hotel = input().split(" ")
        if ((direc[0] - int(hotel[1]))**2 + (direc[1] - int(hotel[2]))**2)**0.5 <= 500:
            if money >= int(hotel[3]):
                hotellist.append(hotel[0])
    if hotellist:
        print(len(hotellist))
        for hotel in hotellist:
            print(hotel)
    else:
        print("No place to go.")
func()
