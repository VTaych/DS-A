import unittest
from itertools import product
from lcm import lcm, lcm_naive


class TestLCM(unittest.TestCase):
    def test_small(self):
        for (a, b) in product(range(1, 15), repeat=2):
            self.assertEqual(lcm(a, b), lcm_naive(a, b))

    def test_large(self):
        for (a, b, m) in [(28851538, 1183019, 1933053046), (456583, 68989,31499204587)]:
            self.assertEqual(lcm(a, b), m)

    # def test_stress(self):
    #     number_of_iterations = 10
    #     array_size = 100
    #     max_number = 2 * 10 ** 5
    #
    #     for _ in range(number_of_iterations):
    #         numbers = [randint(0, max_number) for _ in range(array_size)]
    #         self.assertEqual(max_pairwise_product(list(numbers)), max_pairwise_product_naive(numbers))



if __name__ == '__main__':
    unittest.main()
