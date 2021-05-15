import unittest

import src.LongestIncreasingSequence as LongestIncreasingSequence

class Test(unittest.TestCase):
    sequence = LongestIncreasingSequence.LongestIncreasingSequence()
    def test_Find(self):      

        result = self.sequence.Find("6 5 5 6 7 7 8 9 10 0 1 3 4  6 3")

        self.assertEqual(result,'0 1 3 4 6')

if __name__ == '__main__':
    unittest.main()
