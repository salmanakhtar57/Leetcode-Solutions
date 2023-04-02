"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

"""

class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()
        
        print(nums1)

Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
# output: [1, 2, 2, 3, 5, 6]

Solution().merge([1], 1, [], 0)
# output: [1]