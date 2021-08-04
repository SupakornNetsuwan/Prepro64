"""Func"""

def bottomhalf(text):
    """Flare Bottom"""
    # bottom half
    for i in range(1, len(text)):
        # print("Y: %d\t" %y, end=" ")
        re_text = text[::-1]
        for j in range(len(text)):
            if j == len(text)-1:
                print(text[i], end=" ")
            else:
                if j+i == len(text)-1:
                    print(re_text[j], end=" ")
                else:
                    print(" ", end=" ")
        for j in range(len(text)):
            if j == i-1:
                print(text[i], end=" ")
            else:
                print(" ", end=" ")
        print()

def tophalf():
    """Flare Top"""
    text = input().upper()
    for i in range(len(text)-1):
        # print("Y: %d\t" %y, end=" ")
        re_text = text[::-1]

        # ซีกซ้ายบน
        for j in range(len(text)-1):
            if j == i:
                print(re_text[j], end=" ")
            else:
                print(" ", end=" ")

        #ตรงกลาง
        if i != len(text)-1:
            print(re_text[i], end=" ")

        # ซีกขวา
        for j in range(len(text)):
            if j+i == len(text)-2:
                print(text[j+1], end=" ")
            else:
                print(" ", end=" ")
        print()

    # ตรงกลางซ้าย
    for i in range(len(text)):
        re_text = text[::-1]
        print(re_text[i], end=" ")

    #ตรงกลางขวา
    for i in range(1, len(text)):
        print(text[i], end=" ")
    print()
    bottomhalf(text)
tophalf()
