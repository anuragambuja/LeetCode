# https://leetcode.com/problems/valid-palindrome/

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]
    

class Solution:
    def isPalindrome(self, s: str) -> bool:   
        #method 1
        s_temp=[temp.lower() for temp in s if temp in string.ascii_letters + string.digits] 

        #method 2
        s_temp=[temp.lower() for temp in s if temp.isalnum()] 

        #method 3
        s_temp=''.join(temp.lower() for temp in s if temp.isalnum())
        return s_temp == s_temp[::-1]
