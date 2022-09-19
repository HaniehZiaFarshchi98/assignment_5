import random

print("Hello in Game RPS")
userRate = 0
user1Rate = 0
user2Rate = 0
sysRate = 0
kind = int(input("1: game with system or 2: 2 users game?") )

while kind == 1:
    userChoice = input("rock - paper - scissor : (1-2-3) or End Game 4 ?")
    sysChoice = random.randint(1, 3)  # "rock", "paper", "scissor"
    if userChoice == "1" and sysChoice == 1:
        print("system choice : rock")
        print(f"{userRate} - {sysRate}")
    elif userChoice == "1" and sysChoice == 2:
        sysRate += 1
        print("system choice : paper")
        print(f"{userRate} - {sysRate}")
    elif userChoice == "1" and sysChoice == 3:
        userRate += 1
        print("system choice : scissor")
        print(f"{userRate} - {sysRate}")
    # -------------------------
    elif userChoice == "2" and sysChoice == 1:
        userRate += 1
        print("system choice : rock")
        print(f"{userRate} - {sysRate}")
    elif userChoice == "2" and sysChoice == 2:
        print("system choice : paper")
        print(f"{userRate} - {sysRate}")
    elif userChoice == "2" and sysChoice == 3:
        sysRate += 1
        print("system choice : scissor")
        print(f"{userRate} - {sysRate}")
    # -------------------------
    elif userChoice == "3" and sysChoice == 1:
        sysRate += 1
        print("system choice : rock")
        print(f"{userRate} - {sysRate}")
    elif userChoice == "3" and sysChoice == 2:
        userRate += 1
        print("system choice : paper")
        print(f"{userRate} - {sysRate}")
    elif userChoice == "3" and sysChoice == 3:
        print("system choice : scissor")
        print(f"{userRate} - {sysRate}")
    elif userChoice == "4":
        break
    else:
        print("Invalid Choice")
if userRate > sysRate:
    print("Won")
elif userRate < sysRate:
    print("Los")
else:
    print("Equal")
print(f"You Rate : {userRate}\nSystem Rate : {sysRate}")


while kind == 2:
    user1Choice = input("rock - paper - scissor : (1-2-3) or End Game 4 ?")
    user2Choice = input("rock - paper - scissor : (1-2-3) or End Game 4 ?")
    if user1Choice == "1" and user2Choice == "1":
        print(f"{user1Rate} - {user2Rate}")
    elif user1Choice == "1" and user2Choice == "2":
        user2Rate += 1
        print(f"{user1Rate} - {user2Rate}")
    elif user1Choice == "1" and user2Choice == "3":
        user1Rate += 1
        print(f"{user1Rate} - {user2Rate}")
    # -------------------------
    elif user1Choice == "2" and user2Choice == "1":
        user1Rate += 1
        print(f"{user1Rate} - {user2Rate}")
    elif user1Choice == "2" and user2Choice == "2":
        print(f"{user1Rate} - {user2Rate}")
    elif user1Choice == "2" and user2Choice == '3':
        user2Rate += 1
        print(f"{user1Rate} - {user2Rate}")
    # -------------------------
    elif user1Choice == "3" and user2Choice == '1':
        user2Rate += 1
        print(f"{user1Rate} - {user2Rate}")
    elif user1Choice == "3" and user2Choice == '2':
        user1Rate += 1
        print(f"{user1Rate} - {user2Rate}")
    elif user1Choice == "3" and user2Choice == '3':
        print(f"{user1Rate} - {user2Rate}")
    elif user1Choice == "4":
        break
    else:
        print("Invalid Choice")
if user1Rate > user2Rate:
    print("Won")
elif user1Rate < user2Rate:
    print("Los")
else:
    print("Equal")
print(f"user1 Rate : {user1Rate}\nuser2 Rate Rate : {user2Rate}")