import unittest
import main


class TestMain(unittest.TestCase):
    def test_input(self):
        true = True
        answer = 5
        guess = 5
        result = main.guessingGame(answer, guess)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
