nums = [1,2,3,4]
ans=[]
for i in range(len(nums)):
    product=1
    for j in range(len(nums)):
            if i==j:
                  continue
            else:
                  product*=nums[j]
    ans.append(product)

print(ans)