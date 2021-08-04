"""Func"""

def func():
    """Find age"""
    def checker(age):
        """Check"""
        if age < 7:
            return "CHILD"
        elif age >= 7 and age < 25:
            return "TEENAGER"
        elif age >= 25 and age < 59:
            return "ADULT"
        else:
            return "ELDER"
    age1 = checker(int(input()))
    age2 = checker(int(input()))
    age3 = checker(int(input()))
    age4 = checker(int(input()))
    age5 = checker(int(input()))
    print("%s\n%s\n%s\n%s\n%s" %(age1, age2, age3, age4, age5))
func()
