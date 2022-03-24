# Uses python3
import sys


def get_change(m):
    coins = [1, 3, 4]

    change = [0 for i in range(m + 1)]

    change[0] = 0

    for i in range(1, m + 1):
        change[i] = sys.maxsize

    for i in range(1, m + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                add_change = change[i - coins[j]]

                if add_change != sys.maxsize and add_change + 1 < change[i]:
                    change[i] = add_change + 1

    if change[m] == sys.maxsize:
        return -1

    return change[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    # print(get_change(34))
    # print(get_change(2))
    # print(get_change(4))
    # print(get_change(0))
    # print(get_change(1000900))
