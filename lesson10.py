"""Chinga Chung"""
import random
choice = "Rock", "Paper", "Scissors"
user_point = 0
pc_point = 0
end = 2
while True:
    user_choice = input("enter the word...:" "(Rock, Paper, Scissors)...>>>")
    print(user_choice)
    pc_choice = (random.choice(choice))
    print(pc_choice)
    if user_choice == "Rock" and pc_choice == "Scissors" or user_choice == "Scissors" and pc_choice == "Paper" or user_choice == "Paper" and pc_choice == "Rock":
        user_point += 1
        print("YOU WIN! PC is", pc_point, "and You are", user_point)
        if user_point == end and user_point < 3 and user_point > 0:
            print("Game Over!! You Win!!!")
            break
        else:
            continue
    elif pc_choice == "Paper" and user_choice == "Rock" or pc_choice == "Scissors" and user_choice == "Paper" or pc_choice == "Rock" and user_choice == "Scissors":
        pc_point += 1
        print("PC WIN! PC is", pc_point, "and You are", user_point)
        if pc_point == end and pc_point < 3 and pc_point > 0:
            print("Game Over!! You Lose!!!")
            break
        else:
            continue
    elif user_choice == pc_choice:
        pc_point += 0
        user_point += 0
        print("Try again! PC is", pc_point, "and You are", user_point)
        continue




