# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def gcd(a, b):
    if b == 0:
        return a
    else:
        aa = a % b

    return gcd(b, aa)


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    lowest_multiple = (a * b) // gcd(a, b)

    return lowest_multiple


if __name__ == '__main__':
    # input_a, input_b = map(int, input().split())
    # print(lcm(input_a, input_b))
    a, b = 456583, 68989
    print(lcm(a,b))