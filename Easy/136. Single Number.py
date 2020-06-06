# https://leetcode.com/problems/single-number/

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4


"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        d = Counter(nums)
        for k,v in d.items():
            if v == 1:
                return k
                
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        d = {}
        for v in set(nums):
            d[v] = nums.count(v)
        
        for k,v in d.items():
            if v ==1:
                return k

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        d = {}
        for v in nums:
            if v in d:
                d[v]=d[v]+1
            else:
                d[v]=1
        
        for k,v in d.items():
            if v ==1:
                return k
            
            
   
