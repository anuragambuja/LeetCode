#  https://leetcode.com/problems/add-strings/

"""

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        number1 = 0
        number2 = 0
        d = {str(i):i for i in range(0,10)}
        for i in range(len1):
            number1 += 10**i * d[num1[::-1][i]]

        for i in range(len2):
            number2 += 10**i * d[num2[::-1][i]]

        return str(number1 + number2)
        
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        number1 = 0
        number2 = 0
        d = {str(i):i for i in range(0,10)}
        for i in range(len1):
            number1 += 10**i * d[num1[::-1][i]]

        for i in range(len2):
            number2 += 10**i * d[num2[::-1][i]]

        return str(number1 + number2)        

