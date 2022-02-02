# rock-paper-scissors game. player vs computer.

"""
Stone beats scissors by breaking. 
Paper beats stone by wrapping it. 
Scissors beat paper by cutting it.

"""

import random

player_name = input("Name: ")
moves = ["r", "p", "s"] # r: rock, p: paper, s: scissors
lap = 0
player_score = 0
pc_score = 0

while lap < 10:
    
    while True:

        player_move = input(f"{player_name}: ")

        if player_move  == "r" or player_move  == "p" or player_move  == "s": # checking the correctness of the entered move
            break
        else:
            print("Please type an appropriate move!")
    
    pc_move = random.choice(moves)
    
    lap += 1
    
    if  player_move ==  "r" and pc_move == "r":
        print(f"Computer: {pc_move} \nDraw\n")

    elif  player_move == "r" and pc_move == "p":
        print(f"Computer: {pc_move} \nWinner: Computer\n")
        pc_score += 1
      
    elif  player_move == "r" and pc_move == "s":
        print(f"Computer: {pc_move} \nWinner: {player_name}\n")
        player_score += 1
    
    elif  player_move == "p" and pc_move == "r":
        print(f"Computer: {pc_move} \nWinner: {player_name}\n")
        player_score += 1
    
    elif  player_move == "p" and pc_move == "p":
        print(f"Computer: {pc_move} \nDraw\n")
    
    elif  player_move == "p" and pc_move == "s":
        print(f"Computer: {pc_move} \nWinner: Computer\n")
        pc_score += 1
    
    elif  player_move == "s" and pc_move == "r":
        print(f"Computer: {pc_move} \nWinner: Computer\n")
        pc_score += 1

    elif  player_move == "s" and pc_move == "p":
        print(f"Computer: {pc_move} \nWinner: {player_name}\n")
        player_score += 1
    
    else:
        print(f"Computer: {pc_move} \nDraw\n")

print(f"Score: {player_name} {player_score} - {pc_score} Computer")