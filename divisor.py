import sys
argc = len(sys.argv)

def div(n:int ,k :int):
    result = (n/k)
    formatted_result = "{:.3f}".format(result)
    return formatted_result
l = []
k = float(sys.argv[1])
for i in range(2,argc):
    n = float(sys.argv[i])
    a = div(n ,k)

    l.append(a)
s = ''
for i in l:
    s += str(i) + ','
print(s)