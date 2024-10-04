# Problem Number : 2
# Solved on : 4 October 2024

# DESCRIPTION
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

#SOLUTION :
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def mergeArray(nums1, nums2):
            nums1 = nums1 + nums2
            nums1 = sorted(nums1)
            length = len(nums1)
            if length % 2 == 0:
                mid = ((length - 1) // 2)
                mid2 = mid + 1
                median = (nums1[mid] + nums1[mid2]) / 2

            else:
                median = nums1[(length -1) //2]

            return median
        x = mergeArray(nums1, nums2)
        return x


#REMARKS

"""
THIS has a time complexity of O(m+n)
"""

