"""String formatting"""
 
def func():
    """Formatter"""
    name = input()
    date = int(input())
    month = int(input())
    year = int(input()) - 543
    print("'%s' %02d/%02d/%04d" %(name, month, date, year))
func()