nums = [100,4,200,1,3,2]
s=set(nums)
max_length=0
for num in s:
    if num-1 in s:
        continue
    
    current=num
    length=1
    while current+1 in s:
            current+=1
            length+=1

max_length=max(max_length,length)
print(max_length)

