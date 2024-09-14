from typing import NamedTuple
import sys

rc = NamedTuple('rc' , [('name' , str) ,('world' , str) , ('height' , int) , ('time', int)])

def line_to_coaster(line):
    roller = line.strip().split(';')
    return tuple(roller)

def coaster_to_line(c):
    return f"{c[0]} ({c[1]}) {c[3]})"

def sort_coaser(l :list):

    s = sorted(l , key =lambda x : (int(x[3]) , -int(x[2]) , x[0]) )
    return s
def main():
    l =[]
    with open(sys.argv[1]) as f:
        for i in f:
            l.append(line_to_coaster(i))

    for i in sort_coaser(l):

        print(coaster_to_line(i))
main()