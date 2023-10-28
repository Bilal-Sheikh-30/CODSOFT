import random
print('Enter "e" to end game')
while True:
    print("""
    r--->   Rock
    p--->   Paper
    s--->   Scissor""")
    comp = random.choice(['r','s','p'])
    pl1 = input("\nplayer ---> ").lower()
    if pl1 == 'e':
        break
    else:
        if (pl1 == "r" and comp == "s") or (pl1 == "s" and comp == "p") or (pl1 == "p" and comp == "r"):
            print("\nplayer 1:", pl1)
            print('Computer:', comp)
            print("player 1 won")
            print('*'*66)
        elif pl1 == comp:
            print("\nplayer 1:",pl1)
            print('Computer:',comp)
            print("game draw")
            print('*' * 66)
        else:
            print("\nplayer 1:", pl1)
            print('Computer:', comp)
            print("Computer won")
            print('*' * 66)
