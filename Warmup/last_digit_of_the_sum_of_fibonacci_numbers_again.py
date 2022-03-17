# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0
    if to_index == 1:
        return 1
    else:
        from_index = from_index % 60
        to_index = to_index % 60
        b = 0
        for i in range(from_index, to_index+1):
            a = last_digit_of_fibonacci_number(i)
            b += a
        return b % 10


def last_digit_of_fibonacci_number(n):
    # if n < 2:
    #     return n
    previous, current = 0, 1
    num = n % 60
    if n <= 1:
        return n

    for i in range(2, num + 2):
        previous, current = current, previous + current

    return (previous * current) % 10
    # a, b, c = 1, 1, 0
    # for d in bin(n)[3:]:
    #     num = b * b
    #     a, b, c = a * a + num, (a + c) * b, num + c * c
    #
    #     if d == '1':
    #         a, b, c = a + b, a, b
    #
    # return b

    # lst = [0, 1]
    # for i in range(2, to_index + 1):
    #     next_num = lst[i - 1] + lst[i - 2]
    #     lst.append(next_num)
    # return sum(lst[from_index:to_index+1]) % 10


if __name__ == '__main__':
    # input_from, input_to = map(int, input().split())
    # print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(1234, 12345))
