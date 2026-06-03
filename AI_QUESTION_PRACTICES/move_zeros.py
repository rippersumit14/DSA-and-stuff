# input array
nums = [0, 1, 0, 3, 12]

# position to insert non-zero numbers
insert_pos = 0

# move non-zero elements forward
for i in range(len(nums)):

    if nums[i] != 0:
        nums[insert_pos] = nums[i]
        insert_pos += 1

# fill remaining positions with 0
while insert_pos < len(nums):
    nums[insert_pos] = 0
    insert_pos += 1

# final array
print(nums)


