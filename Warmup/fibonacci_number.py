# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    lst = [0, 1]
    for i in range(2, n+1):
        next_num = lst[i - 1] + lst[i - 2]
        lst.append(next_num)
    return lst[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

