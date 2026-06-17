s = "anagram"
t = "nagaram"
dict1={}
dict2={}

if len(s) != len(t):
    print(False)

for ch in s:
    dict1[ch]=dict1.get(ch,0)+1

for ch in t:
    dict2[ch]=dict2.get(ch,0)+1

if dict1==dict2:
    print("Valid Anagram")

else:
    print("Not a valid Anagram")
