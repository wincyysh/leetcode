import unittest

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 0
        begining = 0
        ending = 0
        while ending < len(nums):    
            for i in range(begining,ending+1):
                ending = max(i, i+nums[ending])
                begining = ending
                steps += 1
        return steps

class TestJumpFunction(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_jump_case1(self):
        nums = [2,3,0,1,4]
        result = self.solution.jump(nums)
        self.assertEqual(result, 2)  # Expected output for this case
        
    def test_jump_case2(self):
        nums = [2,3,1,1,4]
        result = self.solution.jump(nums)
        self.assertEqual(result, 2)  # Expected output for this case
    
    # Additional test cases for edge cases
    def test_jump_single_element(self):
        nums = [1]
        result = self.solution.jump(nums)
        self.assertEqual(result, 1)
    
    def test_jump_empty_array(self):
        nums = []
        result = self.solution.jump(nums)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()