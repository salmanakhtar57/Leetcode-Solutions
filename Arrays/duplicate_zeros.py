"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
"""

class Solution:
    def duplicateZeros(self, arr) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1
        print(arr)

Solution().duplicateZeros([1,0,2,3,0,4,5,0])
# output: [1, 0, 0, 2, 3, 0, 0, 4]

Solution().duplicateZeros([1,2,3])
# output: [1, 2, 3]