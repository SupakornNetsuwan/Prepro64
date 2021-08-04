"""Func"""

def func():
    """Find score"""
    teacher = input()
    student = input()
    answer = ""
    removedscore = 0

    for i in range(len(teacher)):
        if teacher[i].lower() != student[i].lower():
            answer += "(%s)" %student[i]
            removedscore -= 1
        else:
            answer += student[i]

    if removedscore < -10:
        realscore = 0
    else:
        realscore = 10 + removedscore

    print(answer)
    print("%d/10 (%d)" %(realscore, removedscore))
func()

"""Func"""

# def func():
#     """Find score"""
#     teacher = input()
#     student = input()
#     answer = ""
#     removedscore = 0

#     for i in range(len(teacher)):
#         if teacher[i].lower() != student[i].lower():
#             answer += "(%s)" %student[i]
#             removedscore -= 1
#         else:
#             answer += student[i]

#     if removedscore < -10:
#         realscore = 0
#     else:
#         realscore = 10 + removedscore

#     if removedscore == 0:
#         removedscore = "-0"
#     else:
#         removedscore = str(removedscore)

#     print(answer)
#     print("%d/10 (%s)" %(realscore, removedscore))
# func()
