import unittest
from hangman import HangmanGame

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.game = HangmanGame()
        
    def test_display_word_no_guesses(self):
        self.game.word = "python"
        self.assertEqual(self.game.display_word(), "_ _ _ _ _ _")
