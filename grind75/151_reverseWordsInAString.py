import unittest

class Solution(object):
  def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """

    s = s.strip()
    output = ''
    s = s.split()
    print(s)
    output = " ".join(reversed(s))
    return output

class TestreverseWordsFunciton(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case1(self):
        s = "the sky is blue"
        output = "blue is sky the"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, output)

    def test_case2(self):
        s = "  hello world  "
        output = "world hello"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, output)

    def test_case3(self):
        s = "a good   example"
        output = "example good a"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()