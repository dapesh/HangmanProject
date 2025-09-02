"""Hangman Game with two difficulty levels and 15-second timer per guess."""
import random
WORDS = ["python", "java", "hangman"]
PHRASES = ["open source", "unit testing", "test driven"]

class HangmanGame:
    def __init__(self):
        self.word = ""
        self.guessed_letters = []
        self.lives = 6

    def display_word(self):
        display = []
        for letter in self.word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)
    
    def choose_word(self, level):
        """Choose a word based on level."""
        if level == "1":
            return random.choice(WORDS)
        elif level == "2":
            return random.choice(PHRASES)
        else:
            raise ValueError("Invalid level")
    
    
    def initialize_game(self, level):
        self.word = self.choose_word(level)
        self.guessed_letters = []
        self.lives = 6

    def process_guess(self, guess):
        """Handle a guessed letter."""
        guess = guess.lower()
        if guess in self.word:
            self.guessed_letters.append(guess)
            if all(
                letter in self.guessed_letters or letter == " "
                for letter in self.word
            ):
                return "win"
            return "correct"
        else:
            self.lives -= 1
            if self.lives <= 0:
                return "lose"
            return "wrong"

    def process_timeout(self):
        """Handle timeout event."""
        self.lives -= 1
        if self.lives <= 0:
            return "lose"
        return "timeout"
