"""Func"""

def func():
    """Empire state"""
    levellist = []
    err = False
    while True:
        level = input()
        if level == "-":
            break
        elif int(level) < 1 or int(level) > 5:
            print("Error! Not have this floor.")
            err = True
            break
        else:
            levellist.append(int(level))
    levellist.sort()
    if not err:
        print("OK! Wait please.")
        print("-----")
        print("Lift is arriving!")
        for level in levellist:
            place = {
                "1":"st",
                "2":"nd",
                "3":"rd",
                "4":"th",
                "5":"th"
            }
            print("-----")
            print("Lift is going up!")
            print("-----")
            print("Lift has reached the %d%s floor!" %(level, place[str(level)]))
func()
