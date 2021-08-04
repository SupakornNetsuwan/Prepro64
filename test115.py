"""Func"""

def func():
    """Matrix 2"""
    size = list(map(int, input().split(" ")))
    mylist = []
    for i in range(size[0]):
        mylist.append(list(map(int, input().split(" "))))
    for i in range(size[1]):
        addition = list(map(int, input().split(" ")))
        for j in range(len(addition)):
            mylist[i][j] += addition[j]
    for mem in mylist:
        print("["+" ".join(list(map(str, mem)))+ "]")
func()
