"""Func"""

def func():
    """Ghost"""
    allnumber = int(input())
    five = allnumber//10000
    four = (allnumber%10000)//1000
    three = (allnumber%1000)//100
    two = (allnumber%100)//10
    one = (allnumber%10)//1
    lastfivedigit = five + four + three + two + one
    if (lastfivedigit%10)%2 == 0:
        if (lastfivedigit%10)%4 == 0:
            print("ผีตานี")
        else:
            print("ผีกระหัง")
    else:
        if (lastfivedigit%10)%5 == 0:
            print("ผีกระสือ")
        else:
            print("ผีปอบ")
func()
