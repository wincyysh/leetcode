import unittest;

class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = ''.join(c for c in s if c.isalnum())
    s = s.lower()
    if s == '':
      return True
    i = 0
    for c in reversed(s):
      if c == s[i]:
        i += 1
      else:
        return False
    return True
  
class TestIsPalindromeFunction (unittest.TestCase):
  def setUp(self):
    self.solution = Solution()
  
  def test_case1(self):
    s = "A man, a plan, a canal: Panama"
    output = True
    result = self.solution.isPalindrome(s)
    self.assertEqual(result, output)
  def test_case2(self):
    s = "race a car"
    output = False
    result = self.solution.isPalindrome(s)
    self.assertEqual(result, output)
  def test_case3(self):
    s = " "
    output = True
    result = self.solution.isPalindrome(s)
    self.assertEqual(result, output)
  def test_case4(self):
    s = "0P"
    output = False
    result = self.solution.isPalindrome(s)
    self.assertEqual(result, output)

if __name__ == '__main__':
  unittest.main()