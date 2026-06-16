nums = [1,1,2,2,3,4]
flag = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):

        if nums[i] == nums[j]:
            flag = 1
if flag == 1:
    print(True)
else:
    print(False)


#2nd Method
if len(nums) != len(set(nums)):
    print(True)
else:
    print(False)