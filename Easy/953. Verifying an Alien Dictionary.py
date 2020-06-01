# https://leetcode.com/problems/verifying-an-alien-dictionary/

"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

"""

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if len(IP.split('.')) == 4:
            return 'IPv4' if all([True if x.isdigit() 
                                  and 255 >= int(x) >=0 
                                  and len(x) == len(str(int(x))) 
                                  else False 
                                  for x in IP.split('.')]) else 'Neither'
        elif len(IP.split(':')) == 8:
            import string
            return 'IPv6' if all([True if 0 < len(x) <= 4 
                                  and all(c in string.hexdigits for c in x)
                                  else False 
                                  for x in IP.split(':')]) else 'Neither'
        return 'Neither'
        
        
class Solution(object):
    def validIPAddress(self, IP):
        ip_list = IP.split(".")
        if len(ip_list) == 4:
            for group in ip_list:
                try:
                    n = int(group)
                    if n < 0 or n > 255 or len(str(n)) != len(group):
                        return "Neither"
                except:
                    return "Neither"
            return "IPv4"
            
        ip_list = IP.split(":")
        if len(ip_list) != 8:
            return "Neither"
        
        for group in ip_list:
            try:
                n = int(group, 16)
                if n < 0 or n > int("FFFF", 16) or len(group) > 4 or group[0] == "-":
                    return "Neither"
            except:
                return "Neither"
        
        return "IPv6"
