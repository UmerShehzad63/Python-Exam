import sys
d = {}
for s in sys.stdin:
    l = s.strip().split(":")
    name = l[0]

    a = l[1].split(',')
    attractions = len(a)
    d[name] = attractions



for i ,j in sorted(d.items() , key = lambda x : (int(x[1]) , x[0])):
    print(f"{i} : {j} attraction (s) ")