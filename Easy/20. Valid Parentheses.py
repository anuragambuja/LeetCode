# https://leetcode.com/problems/valid-parentheses/

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""

class Solution:
    def isValid(self, s: str) -> bool:
        lst = list()

        for p in s:
            if (len(lst)>0) and ((p == ')' and lst.pop() == '(') or (p == ']' and lst.pop() == '[') or (p == '}' and                      lst.pop() == '{')):
                continue
            else:
                lst.append(p)
        if lst:
            return False

        return True


