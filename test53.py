"""Func"""

def func():
    """Promotion"""
    ppamount = int(input())
    priceperperson = float(input())
    discount = int(input())

    def method1(priceperperson, ppamount, discount):
        """method 1"""
        if ppamount >= 3:
            return (priceperperson*ppamount) * ((100-discount)/100)
        else:
            return priceperperson * ppamount
    def method2(ppamt, priceperperson):
        """method 2"""
        return (((ppamt // 4)* 3) + ppamt % 4)*priceperperson

    mth1 = method1(priceperperson, ppamount, discount)
    mth2 = method2(ppamount, priceperperson)

    if mth1 < mth2:
        print("Promotion 1 %.3f Baht\
\nPurchase successfully !\
\nHave a good meal with \"Kanomwhan\"" %mth1)
    elif mth2 < mth1:
        print("Promotion 2 %.3f Baht\
\nPurchase successfully !\
\nHave a good meal with \"Kanomwhan\"" %mth2)
    else:
        print("Promotion 1 %.3f Baht\
\nPurchase successfully !\
\nHave a good meal with \"Kanomwhan\"" %mth1)

func()
