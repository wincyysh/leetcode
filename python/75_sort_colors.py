import unittest

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cur = 0
        p0 = 0
        p2 = len(nums)-1
        # nums[0], nums[0] = nums[0], nums[0] is a standard Python swap.
        while cur <= p2: 
            # why when nums[curr] == 0 cur also need to add one?
            # Because curr starts at the same place as p0 and moves at the same speed or faster, 
            # we already know that whatever is at p0 is either a 0 or a 1.
            if nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                p0 += 1
                cur += 1
                # print(nums, "cur == 0")
            elif nums[cur] == 1:
                cur += 1
                # print(nums, "cur == 1")
            else:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                # print(nums, "cur == 2")
                p2 -= 1
        return nums

class TestMerge(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        nums = [2,0,2,1,1,0]
        Output = [0,0,1,1,2,2]
        result = self.solution.sortColors(nums)
        self.assertEqual(result, Output)

    def test_case2(self):
        nums = [2,0,1]
        Output = [0,1,2]
        result = self.solution.sortColors(nums)
        self.assertEqual(result, Output)


if __name__ == '__main__':
    unittest.main()
    # def test_case3(self):

    #     result = self.solution.sortColors(nums)
    #     self.assertEqual(result, Output)