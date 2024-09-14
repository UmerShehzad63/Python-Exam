def sum_f(n:int):
    if n == 2:
        return 88
    else:
        return n*n*n*(n+9) + sum_f(n-1)

def main():
    while True:

        n = int(input())
        if n == 0 :
            break
        else:
            print(sum_f(n))
if __name__ == '__main__':
    main()