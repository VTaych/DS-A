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
    elif to_index == 1:
        return 1
    elif from_index == 0:
        a = last_digit_of_fibonacci_number(from_index)
        b = last_digit_of_fibonacci_number(to_index)
        c = b - a
        return c % 10
    else:
        a = last_digit_of_fibonacci_number(from_index - 1)
        b = last_digit_of_fibonacci_number(to_index)
        c = b - a
    return c % 10


def last_digit_of_fibonacci_number(n):

    previous, current = 0, 1

    if n < 2:
        return n
    else:
        num = n % 60
        if num == 0:
            return 0
        for i in range(2, num + 3):
            temp = (previous + current) % 60
            previous = current
            current = temp

        return current - 1


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
    # print(last_digit_of_the_sum_of_fibonacci_numbers_again(0,0))
    # print(last_digit_of_the_sum_of_fibonacci_numbers_again(0,7))
    # print(last_digit_of_the_sum_of_fibonacci_numbers_again(1234, 12345))
