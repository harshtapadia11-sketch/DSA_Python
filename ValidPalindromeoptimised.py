s = "A man, a plan, a canal: Panama"

s = s.lower()

left = 0
right = len(s) - 1

while left < right:

    if not s[left].isalnum():
        left += 1
        continue

    if not s[right].isalnum():
        right -= 1
        continue

    if s[left] != s[right]:
        print("Not a valid palindrome")
        break

    left += 1
    right -= 1

else:
    print("Valid palindrome")