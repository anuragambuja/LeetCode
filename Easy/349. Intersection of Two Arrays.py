# https://leetcode.com/problems/intersection-of-two-arrays/

"""

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
        
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & (set(nums2)))
        
# if the lists are already sorted which is generally asked

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = list(set(nums1))
        a.sort()
        b = list(set(nums2))
        b.sort()
        lst=[]

        i=0
        j=0
        while i < len(b) and j < len(a):
            if a[j] < b[i]:
                j +=1
            elif a[j] == b[i]:
                lst.append(b[i])
                i+=1
                j+=1

            elif a[j] > b[i]:
                i+=1
        return lst
