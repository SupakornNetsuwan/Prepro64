"""Func"""

def func():
    """Pork maker"""
    mhcount = 0
    phcount = 0
    shcount = 0
    whcount = 0
    wrongcount = 0 #err
    totalcount = 0
    while True:
        ingredient = input().upper()
        if ingredient == "MH":
            mhcount += 1
        elif ingredient == "PH":
            phcount += 1
        elif ingredient == "SH":
            shcount += 1
        elif ingredient == "WH":
            whcount += 1
        elif ingredient != "END" and ingredient != "GH": #else
            mhcount = 0
            phcount = 0
            shcount = 0
            whcount = 0
            wrongcount += 1
        elif ingredient == "GH":
            if (mhcount-1 >= 0) and (phcount-1 >= 0) and (shcount-1 >= 0) and (whcount-1 >= 0):
                mhcount = 0
                phcount = 0
                shcount = 0
                whcount = 0
                totalcount += 1
        elif ingredient == "END":
            i = 1
            while i <= wrongcount:
                print("ERROR")
                i += 1
            print(totalcount)
            break
func()
