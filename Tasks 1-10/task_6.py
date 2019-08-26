def func_task_6(n):
    """
    Сумма квадратов первых десяти натуральных чисел равна

    1^2 + 2^2 + ... + 10^2 = 385
    Квадрат суммы первых десяти натуральных чисел равен

    (1 + 2 + ... + 10)^2 = 552 = 3025
    Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.

    Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
    """

    return sum([x for x in range(1, n + 1)]) ** 2 - sum([x ** 2 for x in range(1, n + 1)])


# Ниже приведены тесты
import unittest


class TestTask6(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_6(10), 2640)

    def test_task(self):
        self.assertEqual(func_task_6(100), 25164150)


if __name__ == '__main__':
    unittest.main()