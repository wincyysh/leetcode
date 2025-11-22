import unittest

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_area = min(height[l], height[r]) * (r - l)

        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            cur_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, cur_area)

        return max_area


class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.solution.maxArea(height), 49)

    def test_case2(self):
        height = [1, 1]
        self.assertEqual(self.solution.maxArea(height), 1)

if __name__ == '__main__':
    unittest.main()