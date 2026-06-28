nums = [100,4,200,1,3,2]

nums.sort()

count = 1
max_count = 1

for i in range(1, len(nums)):
    if nums[i]==nums[i-1]+1:
        count+=1
    elif nums[i]==nums[i-1]:
        continue
    else:
        max_count=max(max_count,count)
        count=1

max_count=max(max_count,count)

print(max_count)