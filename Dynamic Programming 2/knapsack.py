# Uses python3
import sys


def optimal_weight(W, w):

    n = len(w)
    if W == 0:
        return 0
    if n == 0:
        return 0
    if W >= sum(w):
        return sum(w)

    val = [0] + w
    result = {}
    for j in range(0, W+1):
        result[j, 0] = 0
    for i in range(0, len(val)):
        result[0, i] = 0

    for i in range(1, len(val)):
        for j in range(1, W+1):
            result[j, i] = result[j, (i - 1)]

            if val[i] <= j:
                value = result[j - val[i], i - 1] + val[i]

                if result[j, i] < value:
                    result[j, i] = value

    return max(result.values())


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

    # print(optimal_weight(10, [1, 4, 8]))
