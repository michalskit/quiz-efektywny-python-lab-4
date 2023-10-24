import unittest
from lab4_quiz import max_min_difference, next_prime, filter_kwargs

class TestInformatyki(unittest.TestCase):
    
    def test_max_min_difference(self):
        self.assertEqual(max_min_difference(1, 3, 5, 9), 8)
        self.assertEqual(max_min_difference(15, 22, 8, 19, 31), 23)
        self.assertEqual(max_min_difference(4), 0)
        self.assertEqual(max_min_difference(), 0)

    def test_next_prime(self):
        prime_gen = next_prime(10)
        self.assertEqual(next(prime_gen), 11)
        self.assertEqual(next(prime_gen), 13)

        prime_gen = next_prime(1)
        self.assertEqual(next(prime_gen), 2)
        self.assertEqual(next(prime_gen), 3)

    def test_filter_kwargs(self):
        def double(x):
            return x * 2

        self.assertEqual(filter_kwargs(double, apple=2, banana=4, avocado=6), {'apple': 4, 'avocado': 12})
        self.assertEqual(filter_kwargs(double, berry=1, melon=2, apricot=3), {'apricot': 6})
        self.assertEqual(filter_kwargs(double, pear=1, peach=2), {})


if __name__ == '__main__':
    unittest.main()
