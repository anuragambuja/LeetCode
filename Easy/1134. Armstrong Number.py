# https://leetcode.com/problems/armstrong-number/

"""
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

 

Example 1:

Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
Example 2:

Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
 

Note:

1 <= N <= 10^8

"""

class Solution:
    def isArmstrong(self, N: int) -> bool:
        return sum([int(x)**len(str(N)) for x in str(N)]) == N



class Solution:
    def isArmstrong(self, N: int) -> bool:
        # Cast N to a list of each digit. E.g. ["1", "2", "3"]
        N_list = list(str(N))
        
		# Compute the value we want to compare to N 
        armstrong_value = sum([int(i) ** len(N_list) for i in N_list])
        
		# See if the value is the same 
        return armstrong_value == N
        
