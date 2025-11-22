import unittest

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i = 0
        if k <= len(nums)-1:
            while i < len(nums)-1:
                for j in range(i+1, i+k+1):
                    if j <= len(nums)-1:
                      if nums[i] == nums[j]:
                          return True
                i += 1
        return False
    

class TestContainsNearbyDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_containsNearbyDuplicate_case1(self):
        nums = [1,2,3,1]
        k = 3
        result = self.solution.containsNearbyDuplicate(nums, k)
        self.assertEqual(result, True)
    
    def test_containsNearbyDuplicate_case2(self):
        nums = [1,0,1,1]
        k = 1
        result = self.solution.containsNearbyDuplicate(nums, k)
        self.assertEqual(result, True)

    def test_containsNearbyDuplicate_case3(self):
        nums = [1,2,3,1,2,3]
        k = 2
        result = self.solution.containsNearbyDuplicate(nums, k)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()