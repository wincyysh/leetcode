class Solution(object):

    # def fromPosition(self, position, nums):
    #     if position == len(nums) - 1: return True
    #     furthest = min(position+nums[position], len(nums)-1)
    #     for nextPosition in range(position+1, furthest+1):
    #         if self.fromPosition(nextPosition, nums): return True
    #     return False
    # def canJump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     return self.fromPosition(0,nums)

    def canJump(self, nums):
        ending = len(nums)-1
        for i in range(ending, -1, -1):
            if i+nums[i] >= ending:
                ending = i
        return True if ending == 0 else False

