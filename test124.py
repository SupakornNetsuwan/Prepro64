"""Func"""

def func():
    """X burner"""
    itemsneed = ["X-gloves", "Leon's tail", "Bullet", "Contact lens", "Ring", "Reborn", "Tsuna"]
    while True:
        items = input()
        if items.lower() == "end":
            break
        for item in items.split(","):
            if item.strip() in itemsneed:
                itemsneed.remove(item.strip())
    if itemsneed:
        print("NO, I have to run!!!")
    else:
        print("X-Burner is ready.")
func()
