import unittest
from collections import OrderedDict
# 146. LRU Cache
# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. 
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:

# inputs
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.


############################### Documentations ###############################
# 4.9.5. Unpacking Argument Lists
# The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:

# list(range(3, 6))            # normal call with separate arguments
# [3, 4, 5]
# args = [3, 6]
# list(range(*args))            # call with arguments unpacked from a list
# [3, 4, 5]

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class TestLRUCache(unittest.TestCase):
    def solution(self, commands, inputs):
        result = []
        obj = None
        for cmd, args in zip(commands, inputs):
            if cmd == "LRUCache":
                obj = LRUCache(*args)
                result.append(None)
            elif cmd == "put":
                obj.put(*args)
                result.append(None)
            else:
                result.append(obj.get(*args))
        return result


    def test_case1(self):
        commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        output = [None, None, None, 1, None, -1, None, -1, 3, 4]
        self.assertEqual(self.solution(commands, inputs), output)

    def test_single_element_cache(self):
        commands = ["LRUCache", "put", "get", "put", "get", "get"]
        inputs   = [[1], [1, 10], [1], [2, 20], [1], [2]]
        expected = [None, None, 10, None, -1, 20]

        self.assertEqual(self.solution(commands, inputs), expected)

    def test_case2(self):
        commands = ["LRUCache", "get"]
        inputs   = [[2], [99]]
        expected = [None, -1]

        self.assertEqual(self.solution(commands, inputs), expected)

    def test_overwrite_existing_key(self):
        commands = ["LRUCache", "put", "put", "get"]
        inputs   = [[2], [1, 1], [1, 99], [1]]
        expected = [None, None, None, 99]

        self.assertEqual(self.solution(commands, inputs), expected)

if __name__ == '__main__':
    unittest.main()