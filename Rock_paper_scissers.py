#game rock paper scissors

#players input

while True:
    print("This is a rock paper scissors game.")
    player_1 = str(input("Player 1 choose and write rock, paper or scissors: "))
    player_2 = str(input("Player 2 Choose and write rock, paper or scissors: "))
    if player_1 == "rock" and player_2 == "rock":
        print("Drawn, nobody won")
    elif player_1 == "rock" and player_2 == "paper":
        print("Congratulation, Player 2 win")
    elif player_1 == "rock" and player_2 == "scissors":
        print("Congratulation, Player 1 win")
    elif player_1 == "scissors" and player_2 == "rock":
        print("Congratulation, Player 2 win")
    elif player_1 == "scissors" and player_2 == "paper":
        print("Congratulation, Player 1 win")
    elif player_1 == "scissors" and player_2 == "scissors":
        print("Drawn, nobody won")
    elif player_1 == "paper" and player_2 == "rock":
        print("Congratulation, Player 1 win")
    elif player_1 == "paper" and player_2 == "paper":
            print("Drawn, nobody won")
    elif player_1 == "paper" and player_2 == "scissors":
        print("Congratulation, Player 2 win")
    else: 
        if player_1 != "rock" or "paper" or "scissors" or player_2 != "rock" or "paper" or "scissors":
            print("This is wrong word")
            break