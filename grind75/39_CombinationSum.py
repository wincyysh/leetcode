import unittest

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # missing list() the result become [] reference vs copy
                results.append(list(comb))
                # print("results: ", results)
                return
            elif remain < 0:
                # print("remian < 0")
                return
            # missing start in first try
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                # print("i: ", i, "candidates[i]: ", candidates[i])
                backtrack(remain - candidates[i], comb, i)
                # print("remain: ", remain, "remain - candidates[i]: ", remain - candidates[i], "comb: ", comb, "start: ", start, "i: ", i)
                comb.pop()

        backtrack(target, [], 0)

        return results

class TestcombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        candidates = [2,3,6,7]
        target = 7
        Output = [[2,2,3],[7]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(Output, result)
        

    def test_case2(self):
        candidates = [2,3,5]
        target = 8
        Output = [[2,2,2,2],[2,3,3],[3,5]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(Output, result)

    def test_case3(self):
        candidates = [2]
        target = 1
        Output = []
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(Output, result)
        
if __name__ == '__main__':
    unittest.main()


####
# root (target: 8)
# ├── [i:0, v:2] remain: 6
# │   ├── [i:0, v:2] remain: 4
# │   │   ├── [i:0, v:2] remain: 2
# │   │   │   ├── [i:0, v:2] remain: 0 -> ✅ SUCCESS [2,2,2,2]
# │   │   │   ├── [i:1, v:3] remain: -1 -> ❌ FAIL
# │   │   │   └── [i:2, v:5] remain: -3 -> ❌ FAIL
# │   │   ├── [i:1, v:3] remain: 1
# │   │   │   ├── [i:1, v:3] remain: -2 -> ❌ FAIL
# │   │   │   └── [i:2, v:5] remain: -4 -> ❌ FAIL
# │   │   └── [i:2, v:5] remain: -1 -> ❌ FAIL
# │   ├── [i:1, v:3] remain: 3
# │   │   ├── [i:1, v:3] remain: 0 -> ✅ SUCCESS [2,3,3]
# │   │   └── [i:2, v:5] remain: -2 -> ❌ FAIL
# │   └── [i:2, v:5] remain: 1
# │       └── [i:2, v:5] remain: -4 -> ❌ FAIL
# ├── [i:1, v:3] remain: 5
# │   ├── [i:1, v:3] remain: 2
# │   │   ├── [i:1, v:3] remain: -1 -> ❌ FAIL
# │   │   └── [i:2, v:5] remain: -3 -> ❌ FAIL
# │   └── [i:2, v:5] remain: 0 -> ✅ SUCCESS [3,5]
# └── [i:2, v:5] remain: 3
#     └── [i:2, v:5] remain: -2 -> ❌ FAIL
######