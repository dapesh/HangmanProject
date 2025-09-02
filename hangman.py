"""Hangman Game with two difficulty levels and 15-second timer per guess."""

class HangmanGame:
    def __init__(self):
        self.word = ""
        self.guessed_letters = []

    def display_word(self):
        display = []
        for letter in self.word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)
