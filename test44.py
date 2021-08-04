"""Func prepro"""

def func():
    """Dead by Moonlight"""
    player1 = input()
    player2 = input()
    player3 = input()
    player4 = input()
    char1 = input()
    char2 = input()
    char3 = input()
    char4 = input()

    def messsage(player, character):
        """Message"""
        duty = character.replace("Dwight", "teamwork").replace("Megg", "juke")
        duty2 = duty.replace("Clodette", "healing").replace("Jake", "silent")
        print("I'm %s. I'm playing %s." %(player, duty2))
    messsage(player1, char1)
    messsage(player2, char2)
    messsage(player3, char3)
    messsage(player4, char4)
func()
