# As we can see, that we can specify error messages, in the assert statements ...
# ... as well, other than the comment on the test function itself
# Also, we can write tests for errors like IndexError, ValueError and others

# There is a basic difference in assertEqual(... , False) and assertFalse(...)
# The latter one, checks if the passed in function returns any Falsey value, like None, empty list
# While the first one only checks if the passed in function returns False, in particular

import unittest
from V4_act import eat, is_funny, laugh


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

    def test_eat_healthy_boolean(self):
        """is_healthy must be a Boolean Value"""
        with self.assertRaises(ValueError):
            eat('pizza', is_healthy='Who Cares!')

    def test_is_funny_tim(self):
        """Tim should not be funny!"""
        self.assertEqual(is_funny('tim'), False)
        # self.assertFalse(is_funny('tim'),'Tim should not be funny!')

    def test_is_funny_anyone_else(self):
        """Anyone else but Tim, should be funny"""
        self.assertTrue(is_funny('blue'), 'Blue should be funny!')
        self.assertTrue(is_funny('tammy'), 'Tammy should be funny!')
        self.assertTrue(is_funny('sven'), 'Sven should be funny!')

    def test_laugh(self):
        """Checks if the returned value is in the tuple or not"""
        self.assertIn(laugh(), ('Lol', 'Haha', 'Tehehe'))


if __name__ == '__main__':
    unittest.main()
