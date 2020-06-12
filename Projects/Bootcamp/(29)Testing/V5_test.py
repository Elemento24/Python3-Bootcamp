# A question can come that what if we define mega_man in the scope of RobotTests
# In that case, every test will be able to access it.
# But since it would be accesses by all the tests, so any changes done in mega_man...
# ... by any of the test, will access the other tests
# So if we want to create the mega_man before every test runs, we can define it in...
# ... setUp. Same goes for tearDown

import unittest
from V5_robot import Robot


class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot('Mega Man', battery=50)

    def test_charge(self):
        """Test for the charge function"""
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        """Test for the say name function"""
        self.assertEqual(self.mega_man.say_name(), 'I AM MEGA MAN')
        self.assertEqual(self.mega_man.battery, 49)

    def test_learn_skill(self):
        """Test for the learn skill function"""
        self.assertEqual(
            self.mega_man.learn_skill('Swimming', 25),
            'WOAH. I KNOW SWIMMING'
        )
        self.assertEqual(
            self.mega_man.learn_skill('Swimming', 51),
            'Insufficient battery. Please charge and try again'
        )


if __name__ == '__main__':
    unittest.main()
