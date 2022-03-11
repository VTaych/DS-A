# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    # refills = 0
    # if stops[1] < m < d:
    #     return -1
    # elif m >= stops[1]:
    #     d = d - stops[1]
    #     refills = refills + 1
    #     return refills, d
    #
    # return refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    # print(compute_min_number_of_refills(input_d, input_m, input_stops))
    print(compute_min_number_of_refills(950, 400, [200, 375, 550, 750]))
