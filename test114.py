"""Func"""

def func():
    """Matrix"""
    size, pos = list(map(int, (input().split("x")))), list(map(int, (input().split(","))))
    matrix, result = [], []
    for i in range(size[0]):
        rowlist = []
        for j in range(size[1]):
            rowlist.append(input())
            if i == pos[0]-1 and j == pos[1]-1:
                result = [i, j]
        matrix.append(rowlist)
    print("result =", matrix[result[0]][result[1]])
    for mem in matrix:
        print('['+" ".join(mem)+']')
func()
