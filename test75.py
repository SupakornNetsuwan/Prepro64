"""Func"""

def convertsecond(hhh, mmm, sss, ampm):
    """From input to allseconds"""
    newseconds = 0 #convert 12-hours to second
    if ampm == "pm":
        if hhh != 12:
            newseconds = (12 + hhh)*60*60 + mmm*60 + sss #from 5 -> 17
        else:
            newseconds = 12*60*60 + mmm*60 + sss
    else:
        if hhh != 12:
            newseconds = hhh*60*60 + mmm*60 + sss
        else:
            newseconds = 0 + mmm*60 + sss

    # print("newseconds:", newseconds)
    return newseconds

def convertback12(allss):
    """From seconds to 12-hours"""
    hours = allss//60//60%24 #1-24(24 == 0)
    minutes = allss//60%60 #(allss/60/60 - allss//60//60)*60
    seconds = allss%60

    # print(hours, minutes, seconds)
    if hours < 12 and hours != 0:
        days = "am"
    elif hours >= 12 and hours < 24:
        days = "pm"
    else:
        days = "am"

    if hours == 0 or hours == 12:
        hours = 12
    else:
        hours = hours%12
    print("%.2d:%.2d:%.2d %s" %(hours, minutes, seconds, days))

def func():
    """Main func"""
    hhh12 = int(input())
    mmm12 = int(input())
    sss12 = int(input())
    ampm = input()
    add_minutes = int(input())
    add_seconds = int(input())
    additiontimes = (add_minutes*60) + add_seconds
    newtime = convertsecond(hhh12, mmm12, sss12, ampm) + additiontimes
    convertback12(newtime)
func()
