# Uses python3
import sys


def optimal_sequence(n):
    all_indexes = [None] * (n + 1)
    min_operations = [0] + [None] * n

    for i in range(1, n + 1):
        some = i - 1
        min_operations1 = min_operations[some] + 1

        if i % 3 == 0:
            part = i // 3
            operations = min_operations[part] + 1
            if operations < min_operations1:
                some, min_operations1 = part, operations

        if i % 2 == 0:
            part = i // 2
            operations = min_operations[part] + 1
            if operations < min_operations1:
                some, min_operations1 = part, operations

        all_indexes[i], min_operations[i] = some, min_operations1

    sequence = []
    i = n
    while i > 0:
        sequence.append(i)
        i = all_indexes[i]

    return reversed(sequence)


if __name__ == '__main__':
    input_ = sys.stdin.read()
    n = int(input_)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')

    # sequence = list(optimal_sequence(96234))
    # print(len(sequence) - 1)
    # for x in sequence:
    #     print(x, end=' ')
