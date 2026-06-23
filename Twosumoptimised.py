nums = [2,7,11,15]
target = 9
seen = {}

for i in range(len(nums)):
    needed=target-nums[i]
    if needed in seen:
        print(seen[needed],i)
    seen[nums[i]]=i