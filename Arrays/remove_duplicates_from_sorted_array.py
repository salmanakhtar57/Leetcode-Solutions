#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

#Example 1:
#Input: nums = [1,1,2]
#Output: 2, nums = [1,2]

#Example 2:
#Input: nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4]

class Solution:
    def removeDuplicates(self, nums) -> int:
        count = 1
        for i in range(len(nums)-1):
            if(nums[i] != nums[i + 1]):
                nums[count] = nums[i + 1]
                count += 1
        
        return(count)

s = Solution()
print(s.removeDuplicates([1,1,2])) #output: 2
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) #output: 5