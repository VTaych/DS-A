# Uses python3
import sys


def get_majority_element(a, left, right):

    a.sort()
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]

    mid = (len(a)-1) // 2
    left = a[:mid]
    right = a[mid:]

    try:
        while left <= right:
            if len(a) == 1:
                return 1
            if a.count(a[mid]) >= (len(a) // 2) + 1:
                return 1
            else:
                a.remove(a[mid])
            return -1
    except IndexError:
        return 0

    return 0
    # mid = len(elements)//2
    # if elements.count(elements[mid]) >= (len(elements) / 2) + 1:
    #     return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

    # if get_majority_element([512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772], 0, 10) != -1:
    #     print(1)
    # else:
    #     print(0)

