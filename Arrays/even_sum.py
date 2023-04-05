#𝐄𝐯𝐞𝐧 𝐒𝐮𝐦: 𝐀𝐝𝐝 𝐔𝐩 𝐘𝐨𝐮𝐫 𝐋𝐢𝐬𝐭 𝐨𝐟 𝐈𝐧𝐭𝐞𝐠𝐞𝐫𝐬
#Question: Write a function that takes in a list of integers and returns the sum of all even numbers.

# Example:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: 30

# Example:  
# Input: [1, 3, 5, 7, 9]
# Output: 0

def even_numbers(nums):
    even_sum = 0
    for num in nums:
        if num % 2 == 0:
            even_sum += num
    return even_sum

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# output: 30

print(even_numbers([1, 3, 5, 7, 9]))
# output: 0