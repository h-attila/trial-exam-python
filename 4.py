# Write unittests for this function:

import unittest


def greeter(name):
  if len(name):
    return 'Hello, ' + name + '!'
  else:
    return 'Hello, Mr Nobody!'


class TestForExerciseFour(unittest.TestCase):

    def test_CheckGivenName(self):
        self.assertEqual(greeter('Géza'), 'Hello, Géza!')

    def test_CheckGivenDifferentName(self):
        self.assertNotEqual(greeter('Géza'), 'Hello, Misi!')

    def test_CheckGivenEmptyString(self):
        self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

    def test_CheckTypeErrorWithNonStringInput(self):
        self.assertRaises(TypeError, greeter, 12345)


if __name__ == '__main__':
    unittest.main()
