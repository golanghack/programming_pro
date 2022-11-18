import unittest
from get_scope import get_scope


class TestGetScore(unittest.TestCase):
    game_stamps = [{'offset': 0, 'score': {'away': 0, 'home': 0}},
                   {'offset': 4, 'score': {'away': 1, 'home': 0}},
                   {'offset': 10, 'score': {}},
                   {'offset': 13},
                   {'offset': 15, 'score': {'away': 1, 'home': 1}},
                   {'offset': 18, 'score': {'away': 2, 'home': 1}}]

    def test_normal_offset(self):
        self.assertEqual(get_scope(self.game_stamps, 15), (1, 1))

    def test_missing_offset(self):
        self.assertEqual(get_scope(self.game_stamps, 16), (1, 1))
        self.assertEqual(get_score(self.game_stamps, 14), (0, 1))

    def test_negative_offset(self):
        self.assertEqual(get_score(self.game_stamps, -50), (0, 0))

    def test_offset_with_no_score(self):
        self.assertEqual(get_score(self.game_stamps, 13), (0, 1))

    def test_offset_with_no_away_home(self):
        self.assertEqual(get_score(self.game_stamps, 10), (0, 1))

    def test_high_offset(self):
        self.assertEqual(get_score(self.game_stamps, 99999999), (1, 2))

    def test_float_offset(self):
        self.assertEqual(get_score(self.game_stamps, 6.6654), (0, 1))

    def test_offset_no_int(self):
        with self.assertRaises(ValueError):
            get_score(self.game_stamps, "pyshop")


if __name__ == '__main__':
    unittest.main()