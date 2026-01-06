import unittest

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def check(i):
            # Copy the original dictionary to use for this index
            remaining = word_count.copy()
            words_used = 0

            # Each iteration will check for a match in words
            for j in range(i, i + substring_size, word_length):
                sub = s[j : j + word_length]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break

            # Valid if we used all the words
            return words_used == k

        answer = []
        for i in range(n - substring_size + 1):
            if check(i):
                answer.append(i)

        return answer

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

