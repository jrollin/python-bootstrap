from game import Game

from unittest import TestCase

class TestGame(TestCase):

    def test_score_at_start(self):

        game = Game()

        self.assertEqual(0, game.getScore())


    def test_score_increment(self):

        game = Game()
        game.incScore()

        self.assertEqual(1, game.getScore())



if __name__ == '__main__':
    unittest.main()