"""
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

example 1:
Input: arr = [10,2,5,3]
Output: true

example 2:
Input: arr = [3, 1, 7, 11]
Output: false
"""

class Solution:
    def checkIfExist(self, arr) -> bool:
        double = set()
        for i in range(len(arr)):
            if 2*arr[i] in double:
                return True
            double.add(arr[i])
        return False

print(Solution().checkIfExist([10,2,5,3]))
print(Solution().checkIfExist([3, 1, 7, 11]))