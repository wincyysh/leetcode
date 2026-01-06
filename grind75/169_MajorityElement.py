import unittest

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = 0
        candidate = 0
        n = len(nums)

        for i in range(0, n):
            if vote == 0:
                candidate = nums[i]
            vote += 1 if nums[i] == candidate else -1

        return candidate

class TestmajorityElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case1(self):
        nums = [3,2,3]
        Output= 3
        result = self.solution.majorityElement(nums)
        self.assertEqual(Output, result)

    def test_case2(self):
        nums = [2,2,1,1,1,2,2]
        Output= 2
        result = self.solution.majorityElement(nums)
        self.assertEqual(Output, result)
    
if __name__ == '__main__':
    unittest.main()