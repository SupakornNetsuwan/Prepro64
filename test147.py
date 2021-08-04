"""Func"""

def func():
    """Matrix V.3"""
    rowcol = list(map(int, input().split(" ")))
    fullmatrix = []
    for i in range(rowcol[0]):
        matrix1 = list(map(int, input().replace("[", "").replace("]", "").split(", ")))
        fullmatrix.append(matrix1)

    newmatrix = []
    for i in range(rowcol[1]):
        newrow = []
        for j in range(rowcol[0]):
            newrow.append((i, j))
        newmatrix.append(newrow)

    for row in range(len(fullmatrix)):
        for column in range(len(fullmatrix[row])):
            newmatrix[column][row] = fullmatrix[row][column]
    for row in newmatrix:
        print(row)
func()
