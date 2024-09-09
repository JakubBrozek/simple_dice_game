import random

agree = input("Do you wanna play? ")

def enemys_turn():
    turn_score = 0
    print("It's enemy's turn!")
    enemy_decision = 1
    while enemy_decision == 1:
        input("Enemy decided to roll")
        enemy_decision = random.randint(0, 1)
        roll_result = random.randint(1, 6)
        print("Enemy rolled: " + str(roll_result))
        if roll_result == 1:
            print('Enemy lost his turn!')
            return 0
        else:
            turn_score += roll_result
    return turn_score

if agree == "Y" or agree == "y":
    player_score = 0
    enemy_score = 0
    next_turn = False
    for turn in range(5):
        turn_score = 0
        print("Turn no. " + str(turn + 1))
        while not next_turn:
            roll_or_out = input("(R)oll or (O)ut? ")
            if roll_or_out == "R" or roll_or_out == "r":
                roll_result = random.randint(1, 6)
                print("You rolled: " + str(roll_result))
                if roll_result == 1:
                    print("Your score hasn't changed: " + str(player_score))
                    next_turn = True
                else:
                    turn_score += roll_result
                    print("Your points for this round: " + str(turn_score))
            else:
                player_score += turn_score
                print("Your score is: " + str(player_score))
                next_turn = True
        enemy_score += enemys_turn()
        next_turn = False
        print("Enemy score: " + str(enemy_score) + ", now it's your turn! B")

    print("THE GAME IS OVER!!!!!")
    print("Player: " + str(player_score) + "Enemy: " + str(enemy_score))
    if player_score < enemy_score:
        print("Player is the WINNER!!")
    elif player_score == enemy_score:
        print("There is a DRAW O.O")
    else:
        print("That was close! But Enemy is the winner!")
