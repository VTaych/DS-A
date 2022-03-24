# Uses python3
import sys
import itertools


def partition3(A):
    # for c in itertools.product(range(3), repeat=len(A)):
    #     sums = [None] * 3
    #     for i in range(3):
    #         sums[i] = sum(A[b] for b in range(len(A)) if c[b] == i)
    #
    #     if sums[0] == sums[1] and sums[1] == sums[2]:
    #         return 1
    #
    # return 0

    if sum(A) % 3 or len(A) < 3:
        return 0

    else:
        answer = sum(A)
        fraction = answer // 3
        table = [[0] * (len(A) + 1) for _ in range(fraction + 1)]

        for i in range(1, fraction + 1):
            for j in range(1, len(A) + 1):
                k = i - A[j - 1]
                if A[j - 1] == i or (k > 0 and table[k][j - 1]):
                    table[i][j] = 1 if table[i][j - 1] == 0 else 2
                else:
                    table[i][j] = table[i][j - 1]

        return 1 if table[-1][-1] == 2 else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
    # print(partition3([3,3,3,3]))
