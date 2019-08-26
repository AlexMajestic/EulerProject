from functools import reduce


def func_task_5(n):
    """
    2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

    Какое самое маленькое число делится нацело на все числа от 1 до 20?
    """
    abs_max = reduce(lambda x, y: x * y, range(1, n + 1))
    divider_list = list(range(11, n))
    result = n

    while result <= abs_max:
        for i in divider_list:
            if result % i != 0:
                break
        else:
            return result
        result += n

# Ниже приведены тесты
import unittest


class TestTask5(unittest.TestCase):
    def test_task(self):
        self.assertEqual(func_task_5(20), 232792560)


if __name__ == '__main__':
    unittest.main()