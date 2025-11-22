import unittest;

class Solution(object):
  def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.find(needle)

class TestStrStrFunction(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test_case1(self):
    haystack = "sadbutsad"
    needle = "sad"
    output = 0
    result = self.solution.strStr(haystack, needle)
    self.assertEqual(result, output)

  def test_case2(self):
    haystack = "leetcode"
    needle = "leeto"
    output = -1
    result = self.solution.strStr(haystack, needle)
    self.assertEqual(result, output)

  def test_case3(self):
    haystack = "abc"
    needle = "c"
    output = 2
    result = self.solution.strStr(haystack, needle)
    self.assertEqual(result, output)

  def test_case4(self):
    haystack = "a"
    needle = "a"
    output = 0
    result = self.solution.strStr(haystack, needle)
    self.assertEqual(result, output)
    
if __name__ == '__main__':
  unittest.main()


# 28. Find the Index of the First Occurrence in a String
# Easy
# Topics
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.