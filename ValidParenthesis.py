s = "([{}])"

stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        
        if not stack or stack[-1] != pairs[ch]:
            print("Not Valid Parenthesis")
            break

        stack.pop()

else:
    if len(stack) == 0:
        print("Valid Parenthesis")
    else:
        print("Not Valid Parenthesis")