import sys
import math

def main():
    for tc in range(int(input())):
        a, b = map(int, input().split())
        x = min(max(2 * a, b), max(a, 2 * b))
        print(x * x)


if __name__ == '__main__':
    main()