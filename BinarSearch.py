nums = [-1,0,3,5,9,12]
target = 3
left=0
right=len(nums)-1
while left<=right:
    middle=(left+right)//2
    if nums[middle]==target:
        print("Element found at index",middle)
    elif nums[middle]<target:
        left=middle+1
    else:
        right=middle-1