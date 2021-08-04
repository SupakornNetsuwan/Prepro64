"""Func"""
############################## piggy boo boo แอดมาเล่นได้ steam ##############################

def func():
    """Apex pack"""
    level = int(input())
    def first(level):
        """1-20"""
        return level-1
    def second(level):
        """21-300"""
        return (level-20)//2
    def third(level):
        """301-500"""
        return (level-300)//5

    if level <= 20:
        print("%d Packs opened\n%d Packs more" %(first(level), 500-first(level)))
    elif level > 20 and level <= 300:
        totalboxs = first(20) + second(level)
        print("%d Packs opened\n%d Packs more" %(totalboxs, 500-totalboxs))
    elif level > 300 and level <= 500:
        totalboxs = first(20) + second(300) + third(level)
        print("%d Packs opened\n%d Packs more" %(totalboxs, 500-totalboxs))
    else:
        totalboxs = first(20) + second(300) + third(500)
        print("%d Packs opened\n%d Packs more" %(totalboxs, 500-totalboxs))
func()
