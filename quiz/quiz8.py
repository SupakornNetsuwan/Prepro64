"""Func"""

def check1(password):
    """check 1"""
    score = 0
    if password.isdigit():
        # print("isdigit")
        score += 50
    if password.isalpha():
        # print("isalphab")
        score += 30
    if password.islower() and password.isalpha():
        # print("islower")
        score += 100
    elif password.isupper() and password.isalpha():
        # print("isupper")
        score += 85
    # password ตัวอักษรในตำแหน่งแรกมีซ้ำกับตัวอักษรอื่นๆใน
    # password มากกว่า 3 ตัว โดยไม่นับตัวแรก (หักคะแนนตัวที่เกินตัวละ 15 คะแนน)
    counterdup = 0
    for i in range(1, len(password)):
        if password[0] == password[i]:
            counterdup += 1
            if counterdup > 3:
                score -= 15
    # ความยาวของ password ที่เกินจาก 10 ตัวอักษร (ตัวละ 10 คะแนน)
    for i in range(len(password) - 10):
        score += 10
    score += ord(password[-1])
    return score

def scorecheck(score):
    """Score check"""
    if score >= 300:
        secure = "secure"
    elif 300 > score >= 150:
        secure = "acceptable"
    elif score < 150:
        secure = "poor"
    return secure

def passwordcheck(password):
    """Password checker"""
    score = 0
    hasalphab, hasnumber = False, False
    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",\
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    score += check1(password)

    # password ประกอบไปด้วยตัวเลข และ ตัวอักษร (75 คะแนน)
    for alphab in lowercase:
        if alphab in password.lower():
            hasalphab = True
            break
    for number in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if number in password:
            hasnumber = True
            break
    if hasalphab and hasnumber:
        score += 75

    # password ประกอบไปด้วยตัวอักษรพิมพ์ใหญ่ และ พิมพ์เล็กเท่านั้น (175 คะแนน)
    hasupper = False
    haslower = False
    if not hasnumber:
        for alphab in lowercase:
            if alphab in password:
                haslower = True
            if alphab.upper() in password:
                hasupper = True
        if hasupper and haslower:
            score += 175

    secure = scorecheck(score)
    print("Password :", "*"*len(password))
    print("Security score :", score)
    print("Security level :", secure)

def func():
    """Strong password"""
    password1 = input()
    if len(password1) < 6:
        print("try again")
        password2 = input()
        if len(password2) < 6:
            print("process terminated")
        else:
            passwordcheck(password2)
    else:
        passwordcheck(password1)
func()
