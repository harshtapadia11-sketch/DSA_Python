a=[2,7,11,15]
target=9
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] == target:
            print(i,j)


#Solution 2nd method

    seen = {}
    for i in range(len(a)):
        needed = target - a[i]
        if needed in seen:
            print([seen[needed], i])
    seen[a[i]] = i