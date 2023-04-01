#Given an array nums of integers, return how many of them contain an even number of digits.

#Example 1:
#Input: nums = [12,345,2,6,7896]
#Output: 2

#Example 2:
#Input: nums = [555,901,482,1771]
#Output: 1

class Solution:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

print(Solution().findNumbers([12,345,2,6,7896]))
print(Solution().findNumbers([555,901,482,1771]))

#solution 2 in one line   
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         return len([x for x in nums if len(str(x)) % 2 == 0])