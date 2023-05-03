#insertion sort
def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

print(selection_sort([2,0,2,1,1,0])) #output: [0, 0, 1, 1, 2, 2]

#Python Built in sort() method
nums = [2,0,2,1,1,0]
nums.sort()
result = nums
print(result) #output: [0, 0, 1, 1, 2, 2]