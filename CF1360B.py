inf = 10 ** 9


def main():
    for tc in range(int(input())):
        n = int(input())
        a = sorted(list(map(int, input().split())))
        mn = inf
        for i in range(len(a) - 1):
            mn = min(mn, a[i + 1] - a[i])
        print(mn)


if __name__ == '__main__':
    main()