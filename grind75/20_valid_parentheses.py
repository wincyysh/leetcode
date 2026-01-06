import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # pipfall: make sure the order of close parenthese then open in mapping
        mapping = {"}":"{",")":"(","]":"["}
        # print(mapping)
        for pa in s:
            if pa in mapping:
                top = stack.pop() if stack else "None"
                # check if the open parentheses same pair as the close parentheses
                if mapping[pa] != top: 
                    return False
            else:
                stack.append(pa)
        # empty list in python is false make sure to add not in front of stack
        return not stack

class TestMerge(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        s = "()"
        Output = True
        result = self.solution.isValid(s)
        self.assertEqual(result, Output)

    def test_case2(self):
        s = "()[]{}"
        Output = True
        result = self.solution.isValid(s)
        self.assertEqual(result, Output)

    def test_case3(self):
        s = "(]"
        Output = False
        result = self.solution.isValid(s)
        self.assertEqual(result, Output)

    def test_case4(self):
        s = "([])"
        Output = True
        result = self.solution.isValid(s)
        self.assertEqual(result, Output)

    def test_case5(self):
        s = "([)]"
        Output = False
        result = self.solution.isValid(s)
        self.assertEqual(result, Output)

    # def test_case(self):

    #     result = self.solution.isValid(s)
    #     self.assertEqual(result, Output)
    
if __name__ == '__main__':
    unittest.main()