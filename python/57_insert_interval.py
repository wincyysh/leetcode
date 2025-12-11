import unittest

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        #case 2 make sure the overlap and merge finish 
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
    
class Testinsert(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        Output = [[1,5],[6,9]]
        result = self.solution.insert(intervals, newInterval)
        self.assertEqual(result, Output)
    
    def test_case2(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        Output = [[1,2],[3,10],[12,16]]
        result = self.solution.insert(intervals, newInterval)
        self.assertEqual(result, Output)



if __name__ == '__main__':
    unittest.main()

