"""Func"""
def func():
    """hint func"""
    hinta = int(input())
    hintb = int(input())
    hintc = int(input())
    hintd = int(input())
    firstnum1 = hinta//10000
    firstnum2 = hintb//10000
    firstnum3 = hintc//10000
    firstnum4 = hintd//10000
    secondnum4 = (hintd//1000)%10
    thirdnum4 = (hintd//100)%10
    fourthnum4 = (hintd//10)%10
    print(firstnum1 + firstnum2 + firstnum3 + firstnum4 + secondnum4 + thirdnum4 + fourthnum4)
func()
