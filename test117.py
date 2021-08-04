"""Func"""

def findcorrect(password):
    """Filter"""
    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",\
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    haslower, hasupper, hasnumber, hasspeical, = False, False, False, False
    for alpha in lowercase:
        if alpha in password:
            haslower = True
        if alpha.upper() in password:
            hasupper = True
    for number in numbers:
        if number in password:
            hasnumber = True
    if ("#" in password or "$" in password or "@" in password) and\
    (" " not in password) and (12 > len(password) >= 6):
        hasspeical = True
    return password if haslower and hasupper and hasnumber and hasspeical and password else False
def func():
    """Password"""
    people = [input(), input(), input()]
    password = input().split(",")
    answer = list(map(findcorrect, password))
    for i in range(len(answer)):
        if answer[i] != False:
            print(answer[i], "("+people[i]+")")
func()
