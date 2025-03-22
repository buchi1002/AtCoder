from collections import deque

def is_balanced(s):
    stack = deque()
    brackets = {')': '(', '}': '{', ']': '[', '>' : '<'}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack

if is_balanced(input()):
    print("Yes")
else:
    print('No')
