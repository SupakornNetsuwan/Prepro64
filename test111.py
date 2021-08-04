"""Func"""

def func():
    """Check for index"""
    mylist = []
    while True:
        alpha = input()
        if alpha.lower() == "end":
            index = int(input())
            if index >= len(mylist):
                print("Index Not Found")
            else:
                print('List[%d] = "%s"' %(index, mylist[index]))
            break
        mylist.append(alpha)
func()
