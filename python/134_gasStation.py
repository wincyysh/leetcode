import unittest;

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        s = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(0, len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                s = i+1
        return s
                

class TestCanCompleteCircuit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        result = self.solution.canCompleteCircuit(gas, cost)
        self.assertEqual(result, 3)
    
    def test_case2(self):
        gas = [2,3,4]
        cost = [3,4,3]
        result = self.solution.canCompleteCircuit(gas, cost)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()