import unittest

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, sum = 0, 0
        res = len(nums) + 1
        for right in range(0, len(nums)):
            sum += nums[right]
            while sum >= target:
                res = min(res, right-left+1)
                sum -= nums[left]
                left += 1
        return res if res != len(nums) + 1 else 0

    
class TestminSubArrayLenFunction(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case1(self):
        target = 7
        nums = [2,3,1,2,4,3]
        result = 2
        self.assertEqual(result, self.solution.minSubArrayLen(target, nums))
    
    def test_case2(self):
        target = 4
        nums = [1,4,4]
        result = 1
        self.assertEqual(result, self.solution.minSubArrayLen(target, nums))

    def test_case3(self):
        target = 11
        nums = [1,1,1,1,1,1,1,1]
        result = 0
        self.assertEqual(result, self.solution.minSubArrayLen(target, nums))

    def test_case4(self):
        nums = [1,2,3,4,5]
        target = 15
        result = 5
        self.assertEqual(result, self.solution.minSubArrayLen(target, nums))

if __name__ == '__main__':
    unittest.main()





# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         left = 0
#         right = 0
#         sumOfCurrentWindow = 0
#         res = float('inf')

#         for right in range(0, len(nums)):
#             sumOfCurrentWindow += nums[right]

#             while sumOfCurrentWindow >= target:
#                 res = min(res, right - left + 1)
#                 sumOfCurrentWindow -= nums[left]
#                 left += 1

#         return res if res != float('inf') else 0