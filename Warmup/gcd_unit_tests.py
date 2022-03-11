import unittest
from gcd import gcd, gcd_naive


class TestGCD(unittest.TestCase):
    def test_small(self):
        for (a, b) in [(1, 1), (2, 6), (3, 9)]:
            self.assertEqual(gcd(a, b), gcd_naive(a, b))

    # def test_stress(self):
    #     number_of_iterations = 10
    #     array_size = 100
    #     max_number = 2 * 10 ** 5
    #
    #     for _ in range(number_of_iterations):
    #         numbers = [randint(0, max_number) for _ in range(array_size)]
    #         self.assertEqual(max_pairwise_product(list(numbers)), max_pairwise_product_naive(numbers))

    def test_large(self):
        for (a, b, d) in [(28851538, 1183019, 17657), (357654894, 134457912, 6)]:
            self.assertEqual(gcd(a, b), d)


if __name__ == '__main__':
    unittest.main()
