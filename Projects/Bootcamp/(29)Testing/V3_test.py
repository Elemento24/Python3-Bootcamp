# This is our test file, which will be used for testing
# If we run this file and all the tests pass, then we will just recieve an 'OK' message
# To see more info in the terminal we can run the file with '-v' flag ...
# like, 'python3 V3_test.py -v' which will see the Comments on Tests as well, if specified

import unittest
from V3_act import eat, nap


class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """Eat should have a Positive Message for Healthy Eating!"""
        self.assertEqual(
            eat('broccoli', is_healthy=True),
            'I am eating broccoli, because my body is a temple!'
        )

    def test_eat_unhealthy(self):
        """Eat should indicate that you have given up for eating unhealthy"""
        self.assertEqual(
            eat('pizza', is_healthy=False),
            'I am eating pizza, because YOLO!'
        )

    def test_short_nap(self):
        """Short naps should be refreshing"""
        self.assertEqual(
            nap(1),
            'I am feeling refreshed after my 1 hour nap!'
        )

    def test_long_nap(self):
        """Long naps should be discouraging"""
        self.assertEqual(
            nap(3),
            'Ugh I overslept. I did not mean to nap for 3 hours!'
        )


if __name__ == '__main__':
    unittest.main()
