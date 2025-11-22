import unittest

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanSymbol = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        roman = ''
        for key, value in sorted(romanSymbol.items(), key = lambda x: x[1], reverse=True):
            print(num//value)
            roman += (num//value)*key
            num %= value
        return roman

class TestIntToRomanFunctino(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_intToRoman_case1(self):
        nums = 3749
        result = self.solution.intToRoman(nums)
        self.assertEqual(result, 'MMMDCCXLIX')  # Expected output for this case
        
    def test_intToRoman_case2(self):
        nums = 58
        result = self.solution.intToRoman(nums)
        self.assertEqual(result, 'LVIII')  # Expected output for this case
    
    # Additional test cases for edge cases
    def test_intToRoman_case3(self):
        nums = 1994
        result = self.solution.intToRoman(nums)
        self.assertEqual(result, 'MCMXCIV')
    


if __name__ == '__main__':
    unittest.main()

