import unittest
from last_digit_of_fibonacci_number import last_digit_of_fibonacci_number, last_digit_of_fibonacci_number_naive


class TestLastDigitOfFibonacciNumber(unittest.TestCase):
    def test_small(self):
        for n in range(20):
            self.assertEqual(last_digit_of_fibonacci_number_naive(n),
                             last_digit_of_fibonacci_number(n))

    # def test_stress(self):
    #     number_of_iterations = 10
    #     array_size = 100
    #     max_number = 2 * 10 ** 5
    #
    #     for _ in range(number_of_iterations):
    #         numbers = [randint(0, max_number) for _ in range(array_size)]
    #         self.assertEqual(max_pairwise_product(list(numbers)), max_pairwise_product_naive(numbers))

    def test_large(self):
        for (n, last_digit) in [(100, 5), (139, 1), (91239, 6), (40, 5)]:
            self.assertEqual(last_digit_of_fibonacci_number(n), last_digit)


if __name__ == '__main__':
    unittest.main()
