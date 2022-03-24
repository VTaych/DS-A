# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    salary = []
    # numbers = [2, 21, 23, 211, 213, 231, 232]
    # salary = numbers.sort(key=lambda x: int(str(x)[0]))


    # biggest = float('-inf')
    # lists = [str(i) for i in numbers]
    # while len(numbers) != 0:
    for i in numbers:
        # salary.append(int(j) for j in i.split()[:])
        # if i >= biggest:

        numbers.sort(key=lambda x: int(str(x)[0]))
        salary = numbers
    return salary

    # first_sequence.sort()
    # second_sequence.sort()
    # c = (i*j for i, j in zip(first_sequence, second_sequence))
    # d = sum(c)
    #
    # return d


if __name__ == '__main__':
    # n = int(input())
    # input_numbers = input().split()
    # assert len(input_numbers) == n
    # print(largest_number(input_numbers))
    print(largest_number([2, 21, 23, 211, 213, 231, 232]))
    print(largest_number([2, 21]))
