import unittest

class Solution(object):
  def fullJustify(self, words, maxWidth):
    res, cur, letterNum = [], [], 0
    for w in words:
      if letterNum + len(w) + len(cur) > maxWidth:
        for i in range(maxWidth - letterNum):
          cur[i%(len(cur)-1 or 1)] += ' '
        res.append(''.join(cur))
        cur, letterNum = [], 0
      cur += [w]
      letterNum += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]
        

class TestfullJustifyFunciton(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test_case1(self):
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    output = ["This    is    an", "example  of text", "justification.  "]
    result = self.solution.fullJustify(words, maxWidth)
    self.assertEqual(result, output)

  def test_case2(self):
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    output = ["What   must   be", "acknowledgment  ", "shall be        "]
    result = self.solution.fullJustify(words, maxWidth)
    self.assertEqual(result, output)

  def test_case3(self):
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    output = ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "]
    result = self.solution.fullJustify(words, maxWidth)
    self.assertEqual(result, output)


if __name__ == '__main__':
   unittest.main()