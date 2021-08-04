"""Func"""

def func():
    """Name"""
    mylist = [] #Normalcase
    mylist2 = [] #lowercase
    while True:
        name = input()
        if name.lower() == "stop":
            break
        if name.isalpha() and name.lower() not in mylist2:
            mylist.append(name)
            mylist2.append(name.lower())
    seq = input().lower()
    if seq.isalpha():
        if seq in mylist2:
            print(mylist2.index(seq) + 1)
        else:
            print("Not found")
    elif seq.isnumeric() and 0 < int(seq) <= len(mylist2):
        print(mylist[int(seq) - 1])
    else:
        print("Not found")
func()
