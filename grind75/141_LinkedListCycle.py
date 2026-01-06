import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes_seen = set()
        current = head
        while current is not None:
            if current in nodes_seen:
                return True
            nodes_seen.add(current)
            current = current.next
        return False


class TesthasCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        # pos = 1        
        # 1. Create the nodes
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)

        # 2. Link them together (3 -> 2 -> 0 -> -4)
        node1.next = node2
        node2.next = node3
        node3.next = node4

        # 3. Create the cycle manually (problem says tail connects to pos 1, which is node2)
        # -4 connects back to 2
        node4.next = node2 

        # 4. Run the solution
        head = node1
        result = self.solution.hasCycle(head)
        Output = True
        self.assertEqual(result, Output)

        # Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

    def test_case2(self):
        # pos = 0
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        node2.next = node1
        head = node1      
        Output = True
        result = self.solution.hasCycle(head)
        self.assertEqual(result, Output)
        # Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

    def test_case3(self):
        # pos = -1
        node1 = ListNode(1)
        head = node1
        Output = False
        result = self.solution.hasCycle(head)
        self.assertEqual(result, Output)
        # Explanation: There is no cycle in the linked list.

if __name__ == '__main__':
    unittest.main()