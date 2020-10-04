import random
import os

win_rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
user_name = input("Enter your name: ")
player_score = 0
print(f"Hello, {user_name}")
score_to_write = ""

#does raitng.txt exist? r reads it, if its not there w+ creates it.
if os.path.isfile("./rating.txt"):
    read = open("rating.txt", "r")
else:
    read = open("rating.txt", "w+")

# Extract player score from old
for line in read:
    if user_name in line:
        player_score = int(line.split()[1])
        continue
    score_to_write += line
read.close()

# ----------------------------------------

# game loop

while True:
    user_input = input().lower()
    if user_input not in win_rules:
        if user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rating":
            print(f"Your rating is: {player_score}")
            continue
        print("Invalid input!")
        continue

    comp_choice = random.choice(list(win_rules))

    if comp_choice == user_input:
        print(f"There is a draw ({user_input})")
        player_score += 50
    elif win_rules[comp_choice] == user_input:
        print(f"Sorry, but the computer chose {comp_choice}")
    else:
        print(f"Well done! Computer chose {comp_choice} and failed")
        player_score += 100
# -------------------------------------------
# Write score on closing
score_to_write += f"{user_name} {player_score}\n"
write = open("rating.txt", "w")
write.write(score_to_write)
write.close()
