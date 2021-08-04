"""Func"""

def func(num, find, counter=0):
    """#3"""
    listnum = list(filter(lambda n: find in n, [j for j in (str(i) for i in range(num+1))]))
    for i in listnum:
        counter += i.count(find)
    print(counter)
func(int(input()), input())
