-- https://leetcode.com/problems/reverse-integer/

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:
    def reverse(self, x: int) -> int:
        if not x >= 2**31-1 or x <= -2**31:  
            if x < 0:
                rev = int('-'+str(x)[1:][::-1])
            else:
                rev = int(str(x)[::-1])
            return 0 if rev >= 2**31-1 or rev <= -2**31 else rev
        else:
            return 0
            
            
class Solution:
    def reverse(self, x: int) -> int:          
        rev = int('-'+str(x)[1:][::-1]) if x < 0 else int(str(x)[::-1])
        return 0 if rev >= 2**31-1 or rev <= -2**31 else rev
        
        
