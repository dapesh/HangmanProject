import unittest
from hangman import HangmanGame, WORDS, PHRASES
import random

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.game = HangmanGame()
        
    def test_display_word_no_guesses(self):
        self.game.word = "python"
        self.assertEqual(self.game.display_word(), "_ _ _ _ _ _")

    def test_level_selection_uses_dictionary(self):
        """Level 1 = WORDS, Level 2 = PHRASES."""
        with self.subTest(level="1"):
            random.choice = lambda xs: xs[0]
            self.assertIn(self.game.choose_word("1"), WORDS)
        with self.subTest(level="2"):
            random.choice = lambda xs: xs[-1]
            self.assertIn(self.game.choose_word("2"), PHRASES)
