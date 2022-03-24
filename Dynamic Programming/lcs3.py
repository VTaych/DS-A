# Uses python3

import sys


def lcs3(a, b, c):
    if len(a) == 0 or len(b) == 0 or len(c) == 0:
        return 0

    d = len(a)
    e = len(b)
    f = len(c)
    check = {}

    for i in range(d + 1):
        for j in range(e + 1):
            for k in range(f + 1):
                if i == 0 or j == 0 or k == 0:
                    check[i, j, k] = 0
                elif a[i - 1] == b[j - 1] and a[i-1] == c[k - 1]:
                    check[i, j, k] = check[i - 1, j - 1, k - 1] + 1
                else:
                    check[i, j, k] = max(max(check[i - 1, j, k], check[i, j - 1, k]), check[i, j, k-1])

    return check[d, e, f]
    # return min(len(a), len(b), len(c))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]

    # a = "geeks"
    # b = "geeksfor"
    # c = "geeksforgeeks"
    print(lcs3(a, b, c))
