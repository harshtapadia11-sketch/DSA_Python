nums = [2,2,1,1,1,2,2]
d={}
for num in nums:
    d[num]=d.get(num,0)+1

max_count=0
answer=0
for key ,value in d.items():
    if value>max_count:
        max_count=value
        answer=key

print(answer)