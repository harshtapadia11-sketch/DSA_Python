nums = [0,1,0,3,12]
# li=[]
# n=[]
# for i in range(len(nums)):
#     if nums[i]!=0:
#         li.append(nums[i])
#     else:
#         n.append(nums[i])
    
# li.extend(n)
# print(li)
j=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        j=j+1

print(nums)