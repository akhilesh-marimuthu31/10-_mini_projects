"""
Rock, Paper, Scissors Game using Tkinter

This is a simple graphical user interface (GUI) version of the classic Rock, Paper, Scissors game.
The user can click on buttons to choose 'Rock', 'Paper', or 'Scissors', and the computer randomly selects 
one of the options. The game will display the result (win, lose, or tie) based on the user's choice 
and the computer's choice.

Tkinter is used to create the GUI, and the game logic is implemented in Python.
"""

import tkinter as tk
import random

# Main function to determine the winner based on the player's choice and computer's random choice
def play(choice):
    # List of possible choices for both the user and the computer
    options = ['Rock', 'Paper', 'Scissors']
    
    # Computer randomly selects one of the options
    computer_choice = random.choice(options)

    # Check if the player's choice and the computer's choice are the same (tie)
    if choice == computer_choice:
        result.set(f"Both chose {choice}. It's a tie!")
    
    # Check if the player's choice beats the computer's choice (win conditions)
    elif (choice == 'Rock' and computer_choice == 'Scissors') or \
         (choice == 'Scissors' and computer_choice == 'Paper') or \
         (choice == 'Paper' and computer_choice == 'Rock'):
        result.set(f"You chose {choice}, Computer chose {computer_choice}. You win!")
    
    # Otherwise, the player loses
    else:
        result.set(f"You chose {choice}, Computer chose {computer_choice}. You lose!")

# Initialize the main window (root) for the application
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")  # Set the window title

# Create and display the game title at the top of the window
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 20), pady=20)
title_label.pack()

# Create a label to display the result of each round (win, lose, or tie)
result = tk.StringVar()  # Tkinter variable to hold dynamic text
result.set("Make your move!")  # Initial text before the game starts
result_label = tk.Label(root, textvariable=result, font=("Arial", 15), pady=20)
result_label.pack()  # Pack the label onto the window

# Create the "Rock" button, which will call the play() function with 'Rock' as the choice
rock_button = tk.Button(root, text="Rock", font=("Arial", 15), width=10, command=lambda: play('Rock'))
rock_button.pack(pady=10)  # Display the button with padding

# Create the "Paper" button, which will call the play() function with 'Paper' as the choice
paper_button = tk.Button(root, text="Paper", font=("Arial", 15), width=10, command=lambda: play('Paper'))
paper_button.pack(pady=10)  # Display the button with padding

# Create the "Scissors" button, which will call the play() function with 'Scissors' as the choice
scissors_button = tk.Button(root, text="Scissors", font=("Arial", 15), width=10, command=lambda: play('Scissors'))
scissors_button.pack(pady=10)  # Display the button with padding

# Start the main loop to run the Tkinter application
root.mainloop()
