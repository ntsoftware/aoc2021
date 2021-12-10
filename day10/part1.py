import sys

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f]

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

def validate_line(line):
    stack = []
    for c in line:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        elif c == '<':
            stack.append('>')
        elif len(stack) == 0:
            # incomplete line
            return 0
        elif c != stack.pop():
            # illegal character
            return scores[c]
    # valid line
    return 0

total_score = sum([validate_line(line) for line in lines])

print(f'Answer: {total_score}')
