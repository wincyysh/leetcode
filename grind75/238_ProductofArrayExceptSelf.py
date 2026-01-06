import unittest

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1]*(n+1)
        suffix = [1]*(n+1)
        answer = [1]*n
        for i in range(1, n+1):
            prefix[i] = prefix[i-1]*nums[i-1]
        # print(prefix)

        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]
        # print(suffix)

        for i in range(0, n):
            answer[i] = prefix[i]*suffix[i+1]
        # print(answer)
        return answer


class TestproductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_productExceptSelf_case1(self):
        nums = [1,2,3,4]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [24,12,8,6])
    
    def test_productExceptSelf_case2(self):
        nums = [-1,1,0,-3,3]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [0,0,9,0,0])


if __name__ == '__main__':
    unittest.main()


# python3 -m unittest productExceptSelf.py