s = "abcabcbb"
seen = set([])
left = 0
max_len = 0

for right in range(len(s)):
    ch=s[right]

    while ch in seen:
        seen.remove(s[left])
        left+=1
    
    seen.add(ch)

    max_len=max(max_len,right-left+1)

print(max_len)