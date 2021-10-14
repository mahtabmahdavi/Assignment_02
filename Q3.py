import random

print("Welcome to 'Palam Pooloum Pilish'")

user_win_count = 0
computer1_win_count = 0
computer2_win_count = 0

for i in range(5):
    print("Select one of them:")
    print("1. ✋")
    print("2. 🤚")

    user_op = int(input("--> "))
    computer1_op = random.randint(1, 2)
    computer2_op = random.randint(1, 2)

    if user_op == 1:
        if computer1_op == 1 and computer2_op == 1:
            print("You: ✋")
            print("Comuter 1: ✋")
            print("Comuter 2: ✋")
        
        elif computer1_op == 1 and computer2_op == 2:
            print("You: ✋")
            print("Comuter 1: ✋")
            print("Comuter 2: 🤚")
            computer2_win_count += 1
        
        elif computer1_op == 2 and computer2_op == 1:
            print("You: ✋")
            print("Comuter 1: 🤚")
            print("Comuter 2: ✋")
            computer1_win_count += 1
        
        elif computer1_op == 2 and computer2_op == 2:
            print("You: ✋")
            print("Comuter 1: 🤚")
            print("Comuter 2: 🤚")
            user_win_count += 1

    elif user_op == 2:
        if computer1_op == 1 and computer2_op == 1:
            print("You: 🤚")
            print("Comuter 1: ✋")
            print("Comuter 2: ✋")
            user_win_count += 1
        
        elif computer1_op == 1 and computer2_op == 2:
            print("You: 🤚")
            print("Comuter 1: ✋")
            print("Comuter 2: 🤚")
            computer1_win_count += 1
        
        elif computer1_op == 2 and computer2_op == 1:
            print("You: 🤚")
            print("Comuter 1: 🤚")
            print("Comuter 2: ✋")
            computer2_win_count += 1
        
        elif computer1_op == 2 and computer2_op == 2:
            print("You: 🤚")
            print("Comuter 1: 🤚")
            print("Comuter 2: 🤚")

if user_win_count < computer1_win_count:
    if computer1_win_count < computer2_win_count:
        print("The computer 2 wins!")
    elif computer1_win_count > computer2_win_count:
        print("The computer 1 wins!")
    elif computer1_win_count == computer2_win_count:
        print("The computer 1 & The computer 2 win!")

elif user_win_count > computer1_win_count:
    if user_win_count < computer2_win_count:
        print("The computer 2 wins!")
    elif user_win_count > computer2_win_count:
        print("Congratulations! You won 🎉")
    elif user_win_count == computer2_win_count:
        print("You & The computer 2 win 🎉")

elif user_win_count == computer1_win_count:
    if user_win_count < computer2_win_count:
        print("The computer 2 wins!")
    elif user_win_count > computer2_win_count:
        print("You & The computer 1 win 🎉")
    elif user_win_count == computer2_win_count:
        print("All of you are equal.")