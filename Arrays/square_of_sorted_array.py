#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#Example 1:
#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]

#Example 2:
#Input: nums = [-7,-3,2,3,11]
#Output: [4,9,9,49,121]

class Solution:
    def sortedSquares(self, nums):
        result = []
        for num in nums:
            result.append(num ** 2)
        result.sort()
        return result
    
print(Solution().sortedSquares([-4,-1,0,3,10])) 
# output: [0,1,9,16,100]

print(Solution().sortedSquares([-7,-3,2,3,11])) 
# output: [4,9,9,49,121]
        