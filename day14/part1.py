import sys

def load(filename):
    with open(filename) as f:
        template = f.readline().strip()
        f.readline()
        rules = dict([line.strip().split(' -> ') for line in f])
        return template, rules

def transform(template, rules):
    result = []
    for i in range(len(template) - 1):
        e = rules.get(template[i:i+2], '')
        result.append(template[i])
        result.append(e)
    result.append(template[-1])
    return ''.join(result)

def frequencies(s):
    return sorted([(e, s.count(e)) for e in set(s)], key=lambda p: p[1])

template, rules = load(sys.argv[1])
print(template)
print(rules)

for i in range(10):
    template = transform(template, rules)
    print(f'After step {i+1}: length={len(template)}')

freqs = frequencies(template)
print(freqs)

print(f'Answer: {freqs[-1][1] - freqs[0][1]}')

