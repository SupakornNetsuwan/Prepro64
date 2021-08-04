"""Func"""
def func():
    """Time format func"""
    second = int(input())
    day = second//(24*60*60)
    hour = (second//3600)%24
    minute = (second//60)%60
    sec = second%60
    print("%02d:%02d:%02d:%02d" %(int(day), int(hour), int(minute), int(sec)))
func()
