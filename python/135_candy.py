import unittest;

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        array = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                array[i] = array[i-1]+1

        for i in range((n-2), -1, -1):
            if ratings[i] > ratings[i+1]:
                array[i] = max(array[i+1]+1, array[i])

        return sum(array)

class TestCandyFunction(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case1(self):
        ratings = [1, 0, 2]
        '''
        array = [2, 1, 2]
        output : 5
        '''
        result = self.solution.candy(ratings)
        self.assertEqual(result, 5)

    def test_case2(self):
        ratings = [1, 2, 2]
        '''
        array = [1, 2, 1]
        output : 4
        '''
        result = self.solution.candy(ratings)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()