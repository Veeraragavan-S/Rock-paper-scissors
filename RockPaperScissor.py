import random

welcome=input("Welcome to the console rock paper scissors game!...\nAre you ready ? ")
if welcome.lower().strip()=="yes":
    print("let's goo...")
else:
    quit()
    
user_points=0
comp_points=0
options=["rock","paper","scissors"]

while True:
    user_pick=input("Type (rock/paper/scissors) to play and Q to quit ").lower()
    
    if user_pick=="q":
        print(f"You scored {user_points} points")
        print(f"Computer scored {comp_points} points")
        if user_points>comp_points:
            print(f"You won:)....you beat computer by {user_points-comp_points} points")
        elif comp_points>user_points:
            print(f"You lost....Computer beat you by {comp_points-user_points} points")
        else:
            print("Match is draw...You and the computer scored equal points %d" %(user_points))
            
        break
    
    elif user_pick not in options:
        print("Type any of these(rock/paper/scissors) only ")
        continue
    else:
        random_num=random.randint(0,2)
        comp_pick=options[random_num]
        print("Computer picked: "+ comp_pick)
        
        if user_pick=="rock" and comp_pick=="scissors":
            user_points+=1
        elif user_pick=="paper" and comp_pick=="rock":
            user_points+=1
        elif user_pick=="scissors" and comp_pick=="paper":
            user_points+=1
        elif (user_pick=="scissors" and comp_pick=="scissors") or (user_pick=="rock" and comp_pick=="rock") or (user_pick=="paper" and comp_pick=="paper"):
            print("Draw")
        else:
            comp_points+=1
            
    