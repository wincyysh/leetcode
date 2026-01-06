import unittest

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        intervals.sort()
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
    
class TestMerge(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output =  [[1,6],[8,10],[15,18]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, Output)

    def test_case2(self):
        intervals = [[1,4],[4,5]]
        Output =  [[1,5]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, Output)
        
    def test_case3(self):
        intervals = [[4,7],[1,4]]
        Output =  [[1,7]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, Output)    

if __name__ == '__main__':
    unittest.main()