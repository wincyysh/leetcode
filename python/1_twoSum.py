import unittest

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         >>> test = Solution()
#         >>> test.twoSum([2,7,11,15], 9)
#         [0,1]
#         >>> test.twoSum([3,2,4], 6)
#         [1,2]
#         >>> test.twoSum([3,3], 6)
#         [0,1]
#         """
#         lnum = len(nums) - 1
#         while lnum > 0:
#             i = lnum
#             for j in range(lnum):
#                 if target - nums[j] == nums[i]:
#                     return [j,i]
#             i -= 1
#             lnum = i
                
#         return []

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []

# class Solution:
#     def twoSum(self, nums, target):
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap:
#                 return [i, hashmap[complement]]
#             hashmap[nums[i]] = i
#         # Return an empty list if no solution is found
#         return []

class TesttwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case1(self):
        nums = [2,7,11,15]
        target = 9
        result = [0,1]
        self.assertEqual(result, self.solution.twoSum(nums, target))

    def test_case2(self):
        nums = [3,2,4]
        target = 6
        result = [1,2]
        self.assertEqual(result, self.solution.twoSum(nums, target))

    def test_case3(self):
        nums = [3,3]
        target = 6
        result = [0,1]
        self.assertEqual(result, self.solution.twoSum(nums, target))

if __name__ == '__main__':
    unittest.main()