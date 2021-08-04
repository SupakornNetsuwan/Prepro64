"""Func"""

def func():
    """vector"""
    answer = []
    for i in range(int(input())):
        int(input())
        vector1 = input()
        vector1 = sorted(list(map(int, vector1[1:len(vector1)-1].split(" "))))
        vector2 = input()
        vector2 = sorted(list(map(int, vector2[1:len(vector2)-1].split(" "))), reverse=True)
        stacker = 0
        for i in range(len(vector1)):
            stacker += vector1[i] * vector2[i]
        answer.append(stacker)

    for i in range(len(answer)):
        print("Case #%d: %d" %(i+1, answer[i]))
func()
