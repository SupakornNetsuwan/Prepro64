"""Func"""

def func():
    """Find sum less than 100"""
    def check(number):
        """Checker"""
        if number > 100:
            return 0
        else:
            return number
    number1 = check(int(input()))
    number2 = check(int(input()))
    number3 = check(int(input()))
    number4 = check(int(input()))
    number5 = check(int(input()))
    number6 = check(int(input()))
    number7 = check(int(input()))
    number8 = check(int(input()))
    number9 = check(int(input()))
    number10 = check(int(input()))
    total = number1+number2+number3+number4+number5+number6+number7+number8+number9+number10
    if total == 420:
        print("herb")
    else:
        print(total)
func()
