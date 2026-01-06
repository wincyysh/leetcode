import unittest;
from collections import Counter

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = right = 0
        nextIndex = {}
        while right < len(s):
            if s[right] in nextIndex:
                left = max(nextIndex[s[right]], left)
            res = max(res, right-left+1)
            nextIndex[s[right]] = right+1
            right += 1
        return res


class TestFunctionLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case1(self):
        case = "abcabcbb"
        result = 3
        self.assertEqual(self.solution.lengthOfLongestSubstring(case), result)
    
    def test_case2(self):
        case = "bbbbb"
        result = 1
        self.assertEqual(self.solution.lengthOfLongestSubstring(case), result)
    
    def test_case3(self):
        case = "pwwkew"
        result = 3
        self.assertEqual(self.solution.lengthOfLongestSubstring(case), result)