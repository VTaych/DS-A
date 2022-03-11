import unittest
from fibonacci_number import fibonacci_number, fibonacci_number_naive


class TestFibonacciNumber(unittest.TestCase):
    def test_small(self):
        for n in range(8):
            self.assertEqual(fibonacci_number(n), fibonacci_number_naive(n))

    # def test_stress(self):
    #     number_of_iterations = 10
    #     array_size = 100
    #     max_number = 2 * 10 ** 5
    #
    #     for _ in range(number_of_iterations):
    #         numbers = [randint(0, max_number) for _ in range(array_size)]
    #         self.assertEqual(fibonacci_number(n), fibonacci_number_naive(n))

    def test_large(self):
        for (n, Fn) in [(30, 832040), (35, 9227465), (40, 102334155)]:
            self.assertEqual(fibonacci_number(n), Fn)


if __name__ == '__main__':
    unittest.main()
