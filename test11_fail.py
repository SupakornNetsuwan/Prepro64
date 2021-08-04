"""Temp func"""

def temp():
    """Convert temp C -> F"""
    celsius = 3545.55387646547564351 
    falenhine = ((celsius * 9)/5 + 32) % 10 # 5.307999
    decimal = int(falenhine * 100)/100 # 5.3
    twodecimal = "%.2f" %decimal # 5.30
    afterdecimal ="%.2f" %(float(twodecimal)%1 * 100)
    print(falenhine)

    switcher = {
        "0.00": int(float(twodecimal))
    }
    answer = switcher.get(afterdecimal, twodecimal)
    # print(answer)

temp()
