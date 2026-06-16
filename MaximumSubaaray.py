nums = [1,2,3]
max_sum = float('-inf')
for i in range(len(nums)):
    current_sum = 0
    for j in range(i, len(nums)):
        current_sum += nums[j]
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)