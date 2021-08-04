"""Convert time"""

def func():
    """find min"""
    inputpass = int(input())
    findsecond = int(float("%.2f" %(inputpass/100000000))%10)
    findfourth = int(float("%.2f" %(inputpass/1000000))%10)
    findsixth = int(float("%.2f" %(inputpass/10000))%10)
    findeighth = int(float("%.2f" %(inputpass/100))%10)
    findtenth = int(inputpass%10)
    print("%d%d%d%d%d" %(findsecond, findfourth, findsixth, findeighth, findtenth))
func()
