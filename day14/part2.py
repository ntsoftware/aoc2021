import sys
from collections import defaultdict

def load(filename):
    with open(filename) as f:
        template = f.readline().strip()
        pairs = defaultdict(int)
        for i in range(len(template) - 1):
            pairs[template[i:i+2]] += 1
        f.readline()
        rules1 = [line.strip().split(' -> ') for line in f]
        rules2 = {src: (src[0] + dest, dest + src[1]) for src, dest in rules1}
        return template, pairs, rules2

def transform(pairs, rules):
    result = defaultdict(int)
    for p,n in pairs.items():
        if p in rules:
            a,b = rules[p]
            result[a] += n
            result[b] += n
        else:
            result[p] += n
    return result

def frequencies(template, pairs):
    freqs = defaultdict(int)
    freqs[template[-1]] = 1
    for p,n in pairs.items():
        freqs[p[0]] += n
    min_freq = min(freqs.values())
    max_freq = max(freqs.values())
    return min_freq, max_freq

template, pairs, rules = load(sys.argv[1])
print(template)
print(pairs)
print(rules)

for i in range(40):
    pairs = transform(pairs, rules)
    print(f'After step {i+1}: length={sum(pairs.values()) + 1}')

min_freq, max_freq = frequencies(template, pairs)
print(f'Answer: {max_freq - min_freq}')

