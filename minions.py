from typing import NamedTuple
import sys


minion = NamedTuple('minion' , [('name' , str) , ('hunger' , int) , ('motivation', int) , ('size' , str)])
def line_to_minion(l :str):
    m = l.strip().split(';')
    return tuple(m)

def minion_to_line(m):
    s = m[0] +' ' + m[1] +' ' + m[3]
    return s

def sort_minions(list : list):

    l = sorted(list , key = lambda x : (-int(x[2]) , x[0]))
    return l


def main():
    list = []

    with open(sys.argv[1]) as f:
        for i in f:
            list.append(line_to_minion(i))

    for i in sort_minions(list):
        print(minion_to_line(i))

main()