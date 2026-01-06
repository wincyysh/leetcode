import unittest




############################ Approach 2: Dynamic Programming, Kadane's Algorithm ########################


########################### python3 #################################
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_a = max_a = nums[0]
        
        for num in nums[1:]:
            cur_a = max(cur_a+num, num)
            max_a = max(max_a, cur_a)

        return max_a

class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        output = 6
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(output, result)

    def test_case2(self):
        output = 1
        nums = [1]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(output, result)

    def test_case3(self):
        output = 23
        nums = [5,4,-1,7,8]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(output, result)


if __name__ == '__main__':
    unittest.main()


################################# C++ ################################
# class Solution {
# public:
#     int maxSubArray(vector<int>& nums) {
#         // Initialize our variables using the first element.
#         int currentSubarray = nums[0];
#         int maxSubarray = nums[0];
#         // Start with the 2nd element since we already used the first one.
#         for (int i = 1; i < nums.size(); i++) {
#             // If current_subarray is negative, throw it away. Otherwise, keep
#             // adding to it.
#             currentSubarray = max(nums[i], currentSubarray + nums[i]);
#             maxSubarray = max(maxSubarray, currentSubarray);
#         }
#         return maxSubarray;
#     }
# };


################################# Approach 1: Optimized Brute Force #################################

################################# C++ ################################
# class Solution {
# public:
#     int maxSubArray(vector<int>& nums) {
#         int max_subarray = INT_MIN;
#         for (int i = 0; i < nums.size(); i++) {
#             int current_subarray = 0;
#             for (int j = i; j < nums.size(); j++) {
#                 current_subarray += nums[j];
#                 max_subarray = max(max_subarray, current_subarray);
#             }
#         }
#         return max_subarray;
#     }
# };

########################### python3 #################################
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_subarray = -math.inf
#         for i in range(len(nums)):
#             current_subarray = 0
#             for j in range(i, len(nums)):
#                 current_subarray += nums[j]
#                 max_subarray = max(max_subarray, current_subarray)

#         return max_subarray


