
xmin,xmax = 124,174
ymin,ymax = -123,-86

def fire(v):
    y = 0
    h = 0
    while True:
        if ymin <= y <= ymax:
            return h
        elif y < ymin:
            return None
        y += v
        v -= 1
        h = max(y,h)

hs = filter(None, [fire(v) for v in range(1000)])

print(f'Answer: {max(hs)}')
