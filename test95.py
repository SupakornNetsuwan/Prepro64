"""Func"""

def func():
    """Inverter"""
    text = input()
    answer = ""
    for i in range(len(text)):
        changetonum = ord(text[i])
        if 57 >= changetonum >= 48: #Number
            if changetonum+5 > 57:
                changetonum = (changetonum+5)%57 + ((changetonum+5)//57 * 47)
            else:
                changetonum += 5
        elif 90 >= changetonum >= 65: #Upper case
            if changetonum+5 > 90:
                changetonum = (changetonum+5)%90 + ((changetonum+5)//90 * 64)
            else:
                changetonum += 5
        elif 122 >= changetonum >= 97: #Lower case
            if changetonum+5 > 122:
                changetonum = (changetonum+5)%122 + ((changetonum+5)//122 * 96)
            else:
                changetonum += 5
        answer += chr(changetonum)
    print(answer)
func()
