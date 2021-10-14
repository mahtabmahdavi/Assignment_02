import random

print("Welcome to 'Rock Paper Scissors'")

user_win_count = 0
computer_win_count = 0

for i in range(5):
    print("Select one of them:")
    print("1. ✊ (Rock)")
    print("2. ✋ (Paper)")
    print("3. ✌ (Scissors)")

    user_op = int(input("--> "))
    computer_op = random.randint(1, 3)

    if user_op == 1 and computer_op == 1:
        print("You: ✊")
        print("Comuter: ✊")

    elif user_op == 1 and computer_op == 2:
        print("You: ✊")
        print("Comuter: ✋")
        computer_win_count += 1

    elif user_op == 1 and computer_op == 3:
        print("You: ✊")
        print("Comuter: ✌")
        user_win_count += 1

    elif user_op == 2 and computer_op == 1:
        print("You: ✋")
        print("Comuter: ✊")
        user_win_count += 1

    elif user_op == 2 and computer_op == 2:
        print("You: ✋")
        print("Comuter: ✋")

    elif user_op == 2 and computer_op == 3:
        print("You: ✋")
        print("Comuter: ✌")
        computer_win_count += 1

    elif user_op == 3 and computer_op == 1:
        print("You: ✌")
        print("Comuter: ✊")
        computer_win_count += 1

    elif user_op == 3 and computer_op == 2:
        print("You: ✌")
        print("Comuter: ✋")
        user_win_count += 1

    elif user_op == 3 and computer_op == 3:
        print("You: ✌")
        print("Comuter: ✌")

if user_win_count < computer_win_count:
    print("The computer wins!")

elif user_win_count > computer_win_count:
    print("Congratulations! You won 🎉")
else:
    print("Both of you are equal.")
