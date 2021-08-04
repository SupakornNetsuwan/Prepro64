"""Func"""

def func():
    """Micheal"""
    stacker = ""
    while True:
        things = input().lower()
        if things == "take care micheal.":
            print("Attack Micheal!!")
            break
        else:
            if things == "chihuahua" or things == "yorkshire terrier" or\
                things == "pug" or things == "dog":
                stacker += "dog"
            elif things == "yorkshire" or things == "duroc" or\
                things == "berkshire" or things == "pig":
                stacker += "pig"
            elif things == "banana bread" or things == "baguette" or\
                things == "breadstick" or things == "bread":
                stacker += "bread"

            if "dogpigbread" in stacker:
                print("Error!!!")
                break
            elif "dog"*5 in stacker or "pig"*5 in stacker or "bread"*5 in stacker:
                print("Stand By")
                break
func()
