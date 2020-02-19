import unittest
import main


class TestMain(unittest.TestCase):
    def test_input(self):
        true = True
        number = 5
        guess = 5
        result = main.guessingGame(number, guess)
        self.assertEqual(result)


if __name__ == "__main__":
    unittest.main()
