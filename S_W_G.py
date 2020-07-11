import random
print("*** SNAKE-WATER-GUN ***")
list = ["Snake", "Water", "Gun"]


n = int(input("Enter number of rounds you want to play: "))
print("--INSTRUCTIONS--\nEnter: S for snake\t W for water\tG for gun\n")

round = 1
U_point=0
C_point= 0

while(round<=n):
    print("---Round:",round, "---")
    user_ch = input("Enter choice(S/W/G):")
    user_ch = user_ch.lower()
    comp_ch = random.choice(list)

    if (user_ch == "s" ) and comp_ch == "Water":
        print("You won this round as computer choose ", comp_ch, "\n")
        U_point = U_point+1
    elif (user_ch == "s") and comp_ch == "Gun":
        print("You loose this round as computer choose", comp_ch, "\n")
        C_point = C_point+1
    elif (user_ch == "s") and comp_ch == "Snake":
        print("Round Tied as computer also selected ", comp_ch, "\n")

    elif (user_ch == "w" ) and comp_ch == "Gun":
        print("You won this round as computer choose ", comp_ch, "\n")
        U_point = U_point+1
    elif (user_ch == "w" ) and comp_ch == "Snake":
        print("You loose this round as computer choose ", comp_ch, "\n")
        C_point = C_point+1
    elif (user_ch == "w") and comp_ch == "Water":
        print("Round Tied as computer also selected ", comp_ch, "\n")

    elif (user_ch == "g" ) and comp_ch == "Snake":
        print("You won this round as computer choose ", comp_ch, "\n")
        U_point = U_point + 1
    elif (user_ch == "g" ) and comp_ch == "Water":
        print("You loose this round as computer choose ", comp_ch, "\n")
        C_point = C_point + 1
    elif (user_ch == "g") and comp_ch == "Gun":
        print("Round Tied as computer also selected ", comp_ch, "\n")
    else:
        print("Enter Valid Input!!(S/W/G)\n")
        continue

    round= round+1


print(f"++++ Final Score ++++\nYou : {U_point} points\nCom: {C_point} points")
if C_point<U_point:
    print(f"Congratulations!! You WON by {U_point-C_point} points")
elif (C_point == U_point):
    print("Game TIED since the points are equal")
else:
    print(f"Game Over!! You LOST by {C_point - U_point} points")
