import unittest

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        return result


class TestcombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        candidates = [2,3,6,7]
        target = 7
        Output = [[2,2,3],[7]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(Output, result)
        

    def test_case2(self):
        candidates = [2,3,5]
        target = 8
        Output = [[2,2,2,2],[2,3,3],[3,5]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(Output, result)

    def test_case3(self):
        candidates = [2]
        target = 1
        Output = []
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(Output, result)
        
if __name__ == '__main__':
    unittest.main()
