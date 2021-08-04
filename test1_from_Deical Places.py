"""String formatting"""

def func():
    """Formatter"""
    name1 = input() #player name    ไม่เกิน 10 ตัว
    hp1 = "O" * int(input()) #player HP ให้แปลงเป็น O * จำนวน HP
    atk1 = int(input()) #ค่า ATK มีตัวละ 4 หลัก เเละต้องเติมเต็มทุกช่อง ถ้าว่างให้เติมด้วย 0
    defend1 = int(input()) #ค่า DEF มีตัวละ 4 หลัก เเละต้องเติมเต็มทุกช่อง ถ้าว่างให้เติมด้วย 0
    name2 = input()
    hp2 = "O" * int(input())
    atk2 = int(input())
    defend2 = int(input())

    print("##############\
\n# %10s #\
\n# HP:%7s #\
\n# ATk || DEF #\
\n# %04d||%04d #\
\n############## VS ##############\
\n                  # %10s #\
\n                  # HP:%7s #\
\n                  # ATk || DEF #\
\n                  # %04d||%04d #\
\n                  ##############" %(name1, hp1, atk1, defend1, name2, hp2, atk2, defend2))

func()
