import unittest
import main


class TestMain(unittest.TestCase):
    def test_input(self):
        number = 5
        guess = 5
        start = 1
        end = 20
        name = "bob"
        result = main.guessingGame(number, guess)
        self.assertEqual(guess, number)


if __name__ == "__main__":
    unittest.main()
