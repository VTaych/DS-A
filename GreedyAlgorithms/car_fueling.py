# python3


def compute_min_number_of_refills(d, m, stops):
    # assert 1 <= d <= 10 ** 5
    # assert 1 <= m <= 400
    # assert 1 <= len(stops) <= 300
    # assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    # refills = 0
    # start = 0
    #
    # if stops[0] > m or d - stops[-1] > m:
    #     return -1

    # for i in range(len(stops) - 1):
    #     d2 = stops[i] - start
    #     start = stops[i]
    #     stops[i] = stops[i + 1]
    #
    #     if stops[i] - stops[i - 1] > m:
    #         return -1
    #     # if d2 > m:
    #     #     return -1
    #     if d2 <= m:
    #         d = d - d2
    #
    #     if d <= m:
    #         return refills
    #
    #     elif d2 <= m:
    #         refills = refills + 1
    #
    # return refills

    refills = 0
    # start = 0

    if stops[0] > m or d - stops[-1] > m:
        return -1

    for i in range(len(stops) - 1):

        start = stops[i]
        stops[i] = stops[i + 1]

        if stops[i] - stops[i - 1] > m:
            return -1

        if d <= m:
            return refills

        else:
            # d2 = stops[i] - start
            refills = refills + 1
            d = d - start

    return refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n
    print(compute_min_number_of_refills(input_d, input_m, input_stops))

    # print(compute_min_number_of_refills(950, 400, [200, 375, 550, 750]))
    # print(compute_min_number_of_refills(10, 3, [1, 2, 5, 9]))
    # print(compute_min_number_of_refills(200, 250, [100, 150]))
    # print(compute_min_number_of_refills(2200, 400, [200, 375, 550, 750, 1150, 1700, 2000]))
    # print(compute_min_number_of_refills(500, 200, [100, 200, 300, 400]))
