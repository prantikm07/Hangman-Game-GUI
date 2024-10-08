import tkinter as tk
from tkinter import messagebox
import random

# Word list
wordlist = ["mango", "apple", "orange", "pineapple", "banana"]

# Hangman stages for visuals
stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]

# Initialize variables
word = random.choice(wordlist)
correct_letters = []
lives = 6
placeholder = "_" * len(word)

# GUI Setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Functions
def update_display():
    display_word = "".join([letter if letter in correct_letters else "_" for letter in word])
    word_label.config(text=display_word)
    
    if "_" not in display_word:
        messagebox.showinfo("Hangman", f"Congratulations! You've guessed the right word: {word}")
        root.quit()

    hangman_canvas.delete("all")
    hangman_canvas.create_text(200, 100, text=stages[6-lives], font=("Courier", 12), fill="black")

def guess_letter():
    global lives
    guess = letter_entry.get().lower()
    letter_entry.delete(0, 'end')

    if len(guess) != 1:
        messagebox.showwarning("Hangman", "Please enter only one letter.")
        return

    if guess in correct_letters:
        messagebox.showwarning("Hangman", "You've already guessed this letter.")
    elif guess in word:
        correct_letters.append(guess)
    else:
        lives -= 1
        if lives == 0:
            messagebox.showerror("Hangman", f"You've lost. The word was: {word}")
            root.quit()

    update_display()

# Input Validation: Limit to a single letter
def limit_input(char):
    return len(char) <= 1 and char.isalpha()

# Labels and Canvas
word_label = tk.Label(root, text=placeholder, font=("Helvetica", 24), bg="#f0f0f0")
word_label.pack(pady=20)

hangman_canvas = tk.Canvas(root, width=400, height=200, bg="#f0f0f0")
hangman_canvas.pack()

# Input Field and Guess Button (center aligned)
vcmd = (root.register(limit_input), '%S')  # Validator for a single letter input
letter_entry = tk.Entry(root, font=("Helvetica", 18), justify='center', validate='key', vcmd=vcmd)
letter_entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess a letter", command=guess_letter, font=("Helvetica", 16), bg="#4CAF50", fg="white")
guess_button.pack(pady=10)

# Center Alignment using pack
letter_entry.pack(pady=10, anchor="center")
guess_button.pack(pady=10, anchor="center")

# Initialize display
update_display()

# Start the game loop
root.mainloop()