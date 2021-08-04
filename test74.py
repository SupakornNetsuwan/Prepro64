"""Func"""

def func():
    """Rock paper scissor"""
    player1 = input()
    player2 = input()
    draw = ("Draw" * (player1 == "Bird" and player2 == "Bird"))\
        +("Draw" * (player1 == "Stone" and player2 == "Stone"))\
        +("Draw" * (player1 == "Water" and player2 == "Water"))
    p1win = ("Sui" * (player1 == "Stone" and player2 == "Bird"))\
        +("Sui" * (player1 == "Water" and player2 == "Stone"))\
        +("Sui" * (player1 == "Bird" and player2 == "Water"))
    p2win = ("Numphung" * (player1 == "Bird" and player2 == "Stone"))\
        +("Numphung" * (player1 == "Stone" and player2 == "Water"))\
        +("Numphung" * (player1 == "Water" and player2 == "Bird"))
    print(draw + p1win + p2win)
func()
