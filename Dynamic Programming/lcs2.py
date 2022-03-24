# Uses python3

import sys


def lcs2(a, b):

    if len(a) == 0 or len(b) == 0:
        return 0

    c = len(a)
    d = len(b)
    check = {}

    for i in range(c + 1):
        for j in range(d + 1):
            if i == 0 or j == 0:
                check[i, j] = 0
            elif a[i - 1] == b[j - 1]:
                check[i, j] = check[i - 1, j - 1] + 1
            else:
                check[i, j] = max(check[i - 1, j], check[i, j - 1])

    return check[c, d]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    # a = "AGGTAB"
    # b = "GXTXAYB"
    # cw = [1, 2, 3]
    # dw = [3, 2, 1]
    print(lcs2(a, b))
    # print(lcs2(c, d))
