from django.test import TestCase

class SmokeTest(TestCase):
    """Toxic."""

    def test_bad_maths(self):
        """Test -> uncorrect maths calc."""

        self.assertEqual(1 + 1, 5)

        
