s = "A man, a plan, a canal: Panama"
cleaned=""
for ch in s.lower():
        if ch.isalnum():
         cleaned+=ch

print(cleaned)

if cleaned==cleaned[::-1]:
     print("Palindrome")

else:
     print("Not a palindrome")