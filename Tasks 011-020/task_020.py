def func_task_20(n):
    """
    n! означает n × (n − 1) × ... × 3 × 2 × 1

    Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Найдите сумму цифр в числе 100!.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i

    return sum(map(int, str(result)))


# Ниже приведены тесты
import unittest


class TestTask20(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_20(10), 27)

    def test_task(self):
        self.assertEqual(func_task_20(100), 648)


if __name__ == '__main__':
    unittest.main()