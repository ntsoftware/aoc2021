import sys

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f]

scores = {')': 1, ']': 2, '}': 3, '>': 4}
closing_chars = {'(': ')', '[': ']', '{': '}', '<': '>'}

def complete_line(line):
    stack = []
    for c in line:
        if c == ')' or c == ']' or c == '}' or c == '>':
            if c != closing_chars[stack.pop()]:
                # illegal character
                return 0
        else:
            stack.append(c)
    if len(stack) == 0:
        # valid line
        return 0
    # incomplete line
    score = 0
    for c in reversed(stack):
        c = closing_chars[c]
        score = score*5 + scores[c]
    return score

sorted_scores = sorted(filter(None, [complete_line(line) for line in lines]))
print(sorted_scores)

print(f'Answer: {sorted_scores[len(sorted_scores) // 2]}')
