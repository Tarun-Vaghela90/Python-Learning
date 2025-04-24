#  day 4  rock paper scissors game
import random
robot_choice = ["rock" , "paper" , "scissors"]

random_choice_robo = random.randint(0,2) 
user = int(input("type 0.rock , 1.paper , 2.scissors  to play game \n"))


if user == 0   and  random_choice_robo  == 0:
    print(f"Robot Choice is {robot_choice[random_choice_robo]}")
    print(f"User Choice is {robot_choice[user]}")
    print("its draw")
elif user == 1   and  random_choice_robo  == 1:
    print(f"Robot Choice is {robot_choice[random_choice_robo]}")
    print(f"User Choice is {robot_choice[user]}")
    print("its draw")
elif user == 2   and  random_choice_robo  == 2:
    print(f"Robot Choice is {robot_choice[random_choice_robo]}")
    print(f"User Choice is {robot_choice[user]}")
    print("its draw")        
elif random_choice_robo == 0  and user == 1:
    print(f"Robot Choice is {robot_choice[random_choice_robo]}")
    print(f"User Choice is {robot_choice[user]}")
    print("You win!")
elif random_choice_robo == 1  and user == 2:
    print(f"Robot Choice is {robot_choice[random_choice_robo]}")
    print(f"User Choice is {robot_choice[user]}")
    print("You win!")
elif random_choice_robo == 2  and user == 0:
    print(f"Robot Choice is {robot_choice[random_choice_robo]}")
    print(f"User Choice is {robot_choice[user]}")
    print("You win!")
else:
    print(f"Robot Choice is {robot_choice[random_choice_robo]}")
    print(f"User Choice is {robot_choice[user]}")
    print("You Loose")