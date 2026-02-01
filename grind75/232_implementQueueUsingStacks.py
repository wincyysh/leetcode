import unittest

class MyQueue(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.instack.append(x)
        return None

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.outstack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop()) 
        return self.outstack[-1]     

    def empty(self):
        """
        :rtype: bool
        """
        if not self.outstack:
            return True
        else:
            return False  



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class TestMyQueue(unittest.TestCase):
    def setUp(self):
        self.solution = MyQueue()

    def test_case1(self):
        # ["MyQueue","push","push","peek","pop","empty"]
        # [[],[1],[2],[],[],[]]
        
        self.solution.push(1)
        self.solution.push(2)
        
        # Test peek
        self.assertEqual(self.solution.peek(), 1)
        
        # Test pop
        self.assertEqual(self.solution.pop(), 1)
        
        # Test empty
        self.assertFalse(self.solution.empty())
        
        # Test last pop
        self.assertEqual(self.solution.pop(), 2)
        self.assertTrue(self.solution.empty())
    
if __name__ == '__main__':
    unittest.main()