import sys
d = {}
with open(sys.argv[1] )as f:
    for s in f:
        l = s.split(";")
        name = l[1]
        price = int(l[3])
        if name in d:
            d[name] += price
        else:
            d[name] = price
for key, value in sorted(d.items() ,key = lambda x: (-int(x[1]) , x[0])):
    print(f"{key} ({value} EUR)")