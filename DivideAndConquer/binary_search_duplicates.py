def binary_search(keys, query):
    a = 0
    b = len(keys) - 1
    while a <= b:
        mid = a + (b - a) // 2
        if keys[mid] == query and keys[mid] > keys[mid - 1]:
            return mid
        elif keys[mid] == query and mid == 0:
            return mid
        elif keys[mid] < query:
            a = mid + 1
        else:
            b = mid - 1
    return -1

    # keys.sort()
    # a = 0
    # b = len(keys) - 1
    #
    # while a <= b:
    #     mid = a + (b - a) // 2
    #     if keys[mid] == query and keys[mid] > keys[mid - 1]:
    #         return mid
    #     elif keys[mid] == query == keys[mid - 1]:
    #         b = mid - 1
    #     elif keys[mid] < query:
    #         a = mid + 1
    #
    # return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

    # keys = [2, 4, 4, 4, 7, 7, 9]
    # queries = [9, 4, 5, 2]
    # for q in queries:
    #     print(binary_search(keys, q), end=' ')

    # print(f"Total runtime of the program is {end - begin}")
