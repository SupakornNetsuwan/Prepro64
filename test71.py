"""Func"""

def func():
    """Car park"""
    dayin = int(input())
    timein = int(input())
    dayout = int(input())
    timeout = int(input())
    totalhour = ((dayout*24)+timeout)-((dayin*24)+timein)

    def findday(tthours):
        """Days"""
        return "%d day %d hour" %(tthours//24, tthours%24)
    def pricecal(tthours):
        """Price"""
        if tthours <= 2:
            return 0
        elif tthours > 2 and tthours <= 12:
            return tthours * 15
        else:
            totaldaypark = tthours//24 #จอดทั้งหมดกี่วัน
            lefthoursprice = 0 #ราคาของชั่วโมง
            if tthours%24 > 12: #ถ้าเศษของวันมากกว่า 12 ชั่วโมงให้คิดราคา 1 วัน
                lefthoursprice = 200
            else:
                lefthoursprice = pricecal(tthours%24) #หาว่าเศษชั่วโมงที่เหลือ คิดกี่บาท

            weeksdiscount = (300*(totaldaypark//7))+(500*(totaldaypark//7 >= 4)) #ราคาส่วนลด
            return (200 * totaldaypark)-weeksdiscount+lefthoursprice

    if dayin*24+timein > dayout*24+timeout or totalhour > 8760 or\
        totalhour > 8760 or dayin < 1 or dayout < 1 or\
        timein >= 24 or timeout >= 24 or dayout > 365 or dayin > 365:
        print("error")
    else:
        print(findday(totalhour))
        print(pricecal(totalhour), "baht")
func()
