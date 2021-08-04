"""String formatting"""
 
def func():
    """Formatter"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    total = num1 + num2 + num3
    print('[" %.2f "]' %total)
func()