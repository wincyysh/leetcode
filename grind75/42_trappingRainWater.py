import unittest;

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max = 0
        leftMax = [0] * n
        rightMax = [0] * n
        trap = [0] * n
        for i in range(0,n):
            if height[i] > max:
                max = height[i]
            leftMax[i] = max
        max = 0
        for i in range(n-1, -1, -1):
            if height[i] > max:
                max = height[i]
            rightMax[i] = max
        print(leftMax)
        print(rightMax)
        for i in range(0, n):
            index = min(leftMax[i],rightMax[i]) - height[i]
            if index >= 0:
                trap[i] = index
            else:
                trap[i] = 0
        return sum(trap)

class  TestTrapFunction(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        result = self.solution.trap(height)
        self.assertEqual(result, 6)

    def test_case2(self):
        height = [4,2,0,3,2,5]
        result = self.solution.trap(height)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()






# 42. Trapping Rain Water
# Hard
# Topics
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105