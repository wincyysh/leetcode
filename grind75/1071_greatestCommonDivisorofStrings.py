import unittest


####################### Approach 1: Brute Force ################################

# class Solution:
#   def gcdOfStrings(self, str1: str, str2: str) -> str:
#     len1, len2 = len(str1), len(str2)

      # if the str1 % base == str2 % base == 0 
#     def valid(k):
#       if len1 % k or len2 % k:
#         return False
#       n1, n2 = len1 // k, len2 // k
#       base = str1[:k]
#       return str1 == n1 * base and str2 == n2 * base 
    
#     for i in range(min(len1, len2), 0, -1):
#       if valid(i):
#         return str1[:i]
#     return ""



####################### Approach 2: Greatest Common Divisor ####################

class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    # def Greatest Common Divisor 
    def gcd(x, y):
      while y != 0:
        (x, y) = (y, x % y)
      return x
    
    # Check if they have non-zero GCD string.    
    if str1 + str2 != str2 + str1:
      return ""

    # Get the GCD of the two lengths.
    max_length = gcd(len(str1), len(str2))
    
    return str1[:max_length]


class TestgcdOfStringsFunction(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test_case1(self):
    str1 = "ABCABC"
    str2 = "ABC"
    output = "ABC"
    result = self.solution.gcdOfStrings(str1,str2)
    self.assertEqual(output, result)

  def test_case2(self):
    str1 = "ABABAB"
    str2 = "ABAB"
    output = "AB"
    result = self.solution.gcdOfStrings(str1, str2)
    self.assertEqual(output, result)

  def test_case3(self):
    str1 = "LEET"
    str2 = "CODE"
    output = ""
    result = self.solution.gcdOfStrings(str1, str2)
    self.assertEqual(output, result)

if __name__ == '__main__':
  unittest.main()