import unittest;

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanSymbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        pre = 0
        cur = 0
        result = 0

        for char in reversed(s):
          cur = romanSymbol[char]
          if cur < pre:
            result += -1 * cur
          else:
            result += cur
          pre = cur
        return result
    
class TestRomanToIntFunciton(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case1(self):
        s = "III"
        result = self.solution.romanToInt(s)
        self.assertEqual(result, 3)

    def test_case2(self):
        s = "LVIII"
        result = self.solution.romanToInt(s)
        self.assertEqual(result, 58)

    def test_case3(self):
        s = "MCMXCIV"
        result = self.solution.romanToInt(s)
        self.assertEqual(result, 1994)

if __name__ == '__main__':
    unittest.main()
