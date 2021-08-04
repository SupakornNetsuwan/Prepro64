"""Func"""

def checkremoved(removedscore):
    """Check for real score"""
    if removedscore < -10:
        realscore = 0
    else:
        realscore = 10 + removedscore

    if removedscore == 0:
        removedscore = "-0"
    else:
        removedscore = str(removedscore)
    return [removedscore, realscore]

def func():
    """Help teacher check"""
    teacher = input()
    student = input()
    arr1 = []
    arr2 = []
    removedscore = 0
    arrans = ""
    for i in range(len(teacher)):
        arr1 += teacher[i]
        arr2 += student[i]

    found = False
    for i in range(len(arr1)):
        if arr1[i].lower() != arr2[i].lower() and found == False:
            if arr1[i+1].lower() == arr2[i+1].lower():
                arrans += "("+arr2[i]+")"
                found = False
                removedscore -= 1
            else:
                arrans += "("+arr2[i]
                found = True
                removedscore -= 1

        elif arr1[i].lower() != arr2[i].lower() and found == True:
            if i == len(arr1)-1:
                if arr1[i].lower() != arr2[i].lower():
                    arrans += arr2[i]+")"
                    found = False
                    removedscore -= 1
            else:
                if arr1[i+1].lower() == arr2[i+1].lower():
                    arrans += arr2[i]+")"
                    found = False
                    removedscore -= 1
                else:
                    arrans += arr2[i]
                    removedscore -= 1
        else:
            arrans += arr2[i]

    score = checkremoved(removedscore)

    print(arrans)
    print("%d/10 (%s)" %(score[1], score[0]))
    #ขี้เกียจทำแล้วครับ ขออภัยในความเละ ;)
func()
