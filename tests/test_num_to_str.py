import unittest
from custom.num_to_str import num_to_str


class TestNtS(unittest.TestCase):
    def setUp(self):
        pass

    def test_111(self):
        self.assertEqual(num_to_str(111), "one hundred and eleven")

    def test_11036(self):
        self.assertEqual(num_to_str(11036), "eleven thousand, thirty six")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num_to_str(
                1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            )


if __name__ == "__main__":
    unittest.main()
