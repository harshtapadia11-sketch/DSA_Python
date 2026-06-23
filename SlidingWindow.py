nums = [2,1,5,1,3,2]
k = 3
maxsum=0
for i in range(len(nums)-k+1):
    currentsum=0
    for j in range(i,i+k):
        currentsum+=nums[j]
        if currentsum>maxsum:
            maxsum=currentsum

print(maxsum)
