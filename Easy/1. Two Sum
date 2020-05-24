# https://leetcode.com/problems/two-sum/

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x,y]
                    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, number in enumerate(nums):

            make_positive = target - number

            if (make_positive in nums) and (nums.index(make_positive) != index):
                return nums.index(make_positive), index
                
                
                           
