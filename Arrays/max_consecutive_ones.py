#Given an array
#Return the max number of consecutive 1s in the array

class Solution:
    def findMaxConsecutiveOnes(self, nums: int, arr):
        count = result = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                result = max(result, count)

        return result