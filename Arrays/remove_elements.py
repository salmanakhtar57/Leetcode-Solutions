#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#Example 1:
#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2]

#Example 2:
#Input: nums = [0,1,2,2,3,0,4,2], val = 2
#Output: 5, nums = [0,1,4,0,3]

class Solution:
    def removeElement(self, nums, val) -> int:
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        nums = nums[:count]
        return count

s = Solution()
print(s.removeElement([3,2,2,3], 3))
#output: 2

print(s.removeElement([0,1,2,2,3,0,4,2], 2))
#output: 5