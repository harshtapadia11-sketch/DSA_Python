nums = [1,2,3,4]
left=[1]*len(nums)
left[0]=1
right = [1] * len(nums)
right[len(nums)-1] = 1
ans=[1]*len(nums)
for i in range(1,len(nums)):
    left[i]=left[i-1] * nums[i-1]

print(left)

for i in range(2,-1,-1):
    right[i]=right[i+1]*nums[i+1]

print(right)

for i in range(len(nums)):
    ans[i]=left[i]*right[i]

print(ans)