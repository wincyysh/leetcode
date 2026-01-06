import unittest

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        i != j, i != k, and j != k
        nums[i] + nums[j] + nums[k] == 0
        [nums[i], nums[j], nums[k]]
        """
        nums = sorted(nums)
        i = 0
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i== 0 or nums[i-1] != nums[i]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j-1] == nums[j]:
                            j += 1
        return res

class TestFunctionThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        case = [0, 1, 1]
        result = []
        self.assertEqual(self.solution.threeSum(case), result)

    def test_2(self):
        case = [0, 0, 0]
        result = [[0,0,0]]
        self.assertEqual(self.solution.threeSum(case), result)

    def test_3(self):
        case = [-1, 0, 1, 2, -1, -4]
        result = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(self.solution.threeSum(case), result)

if __name__ == '__main__':
    unittest.main()