import tkinter as tk
import random


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'


def play(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)

    if result == 'win':
        result_text.set(f"You win! Computer chose {computer_choice}.")
        update_score('user')
    elif result == 'lose':
        result_text.set(f"You lose! Computer chose {computer_choice}.")
        update_score('computer')
    else:
        result_text.set(f"It's a tie! Computer also chose {computer_choice}.")


def update_score(winner):
    global user_score, computer_score
    if winner == 'user':
        user_score += 1
    elif winner == 'computer':
        computer_score += 1

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")


user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors")

result_text = tk.StringVar()
result_text.set("Choose Rock, Paper, or Scissors.")

tk.Label(root, textvariable=result_text).pack()

tk.Button(root, text="Rock", command=lambda: play('rock')).pack()
tk.Button(root, text="Paper", command=lambda: play('paper')).pack()
tk.Button(root, text="Scissors", command=lambda: play('scissors')).pack()

user_score_label = tk.Label(root, text=f"Your Score: {user_score}")
user_score_label.pack()

computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}")
computer_score_label.pack()

root.mainloop()
