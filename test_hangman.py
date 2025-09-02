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

    def test_reveal_all_instances_on_correct_guess(self):
        """Reveal all matching letters."""
        self.game.word = "balloon"
        self.game.guessed_letters = ["l", "o"]
        self.assertEqual(self.game.display_word(), "_ _ l l o o _")

    def test_wrong_guess_deducts_life_and_can_end_game(self):
        """Wrong guess deducts life; zero life = lose."""
        self.game.initialize_game("1")
        self.game.word = "cat"
        self.game.lives = 1
        result = self.game.process_guess("z")
        self.assertEqual(result, "lose")
        self.assertEqual(self.game.lives, 0)

    def test_wrong_guess_deducts_life_and_can_end_game(self):
        """Wrong guess deducts life; zero life = lose."""
        self.game.initialize_game("1")
        self.game.word = "cat"
        self.game.lives = 1
        result = self.game.process_guess("z")
        self.assertEqual(result, "lose")
        self.assertEqual(self.game.lives, 0)

    def test_timeout_deducts_life(self):
        """Timeout deducts life."""
        self.game.initialize_game("2")
        before = self.game.lives
        result = self.game.process_timeout()
        self.assertEqual(result, "timeout")
        self.assertEqual(self.game.lives, before - 1)