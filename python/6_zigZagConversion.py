import unittest

class Solution(object):
    def reverseWords(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        idx=0
        d=1
        rows = [''] * numRows
        if numRows == 1 or idx >= len(s):
            return s
        for char in s:
          rows[idx] += char
          if idx == 0:
            d = 1
          elif idx == numRows-1:
            d = -1
          idx += d
        rows = ''.join(rows)
        return rows
    
class TestreverseWordsFunciton(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case1(self):
        s = "PAYPALISHIRING"
        output = "PAHNAPLSIIGYIR"
        numRows = 3
        result = self.solution.reverseWords(s, numRows)
        self.assertEqual(result, output)

    def test_case2(self):
        s = "PAYPALISHIRING"
        numRows = 4
        output = "PINALSIGYAHRPI"
        result = self.solution.reverseWords(s, numRows)
        self.assertEqual(result, output)

    def test_case3(self):
        s = "A"
        numRows = 1
        output = "A"
        result = self.solution.reverseWords(s, numRows)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()