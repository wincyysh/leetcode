import unittest

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        output = []
        return output

class testFindSubstringFunction(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testCase1(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        result = [0,9]
        self.assertEqual(result, self.solution.findSubstring(s, words))
    
    def testCase2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        result = []
        self.assertEqual(result, self.solution.findSubstring(s, words))

    def testCase3(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        result = [6,9,12]
        self.assertEqual(result, self.solution.findSubstring(s, words))

if __name__ == "__main__":
    unittest.main()