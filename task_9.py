import math


def func_task_9(n):
    """
    Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

    a^2 + b^2 = c^2
    Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    Существует только одна тройка Пифагора, для которой a + b + c = 1000.
    Найдите произведение abc.
    """
    for a in range(2, n):
        for b in range(a + 1, n):
            if a + b > n:
                break

            c = math.sqrt(a ** 2 + b ** 2)
            if c.is_integer() and a + b + c == n:
                return [a, b, int(c)]

    return False

# Ниже приведены тесты
import unittest


class TestTask9(unittest.TestCase):
    def test_task(self):
        self.assertEqual(func_task_9(1000), [200, 375, 425])


if __name__ == '__main__':
    unittest.main()