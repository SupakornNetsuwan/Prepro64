"""Func"""
def func():
    """Find max"""
    inp1 = float(input())
    inp2 = float(input())
    inp3 = float(input())
    inp4 = float(input())
    inp5 = float(input())
    inp6 = float(input())
    inp7 = float(input())
    inp8 = float(input())
    inp9 = float(input())
    inp10 = float(input())
    def greater(num1, num2):
        """finding from two arguments"""
        return ((num1+num2) + abs(num1-num2))/2

    def great(num1, num2, num3):
        """Find a greater number"""
        arg1 = greater(num1, num2)
        arg2 = greater(num2, num3)
        return ((arg1+arg2) + abs(arg1-arg2))/2
    pasd = greater(great(inp1, inp2, inp3), great(inp4, inp5, inp6))
    pasd2 = greater(greater(inp7, inp8), greater(inp9, inp10))
    print("%.2f" %greater(pasd, pasd2))
func()
