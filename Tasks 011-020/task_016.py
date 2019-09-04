def func_task_16(n):
    """
    2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

    Какова сумма цифр числа 2^1000?
    """
    return sum(map(int, str(2 ** n)))


# Ниже приведены тесты
import unittest


class TestTask16(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_16(15), 26)

    def test_task(self):
        self.assertEqual(func_task_16(1000), 1366)


if __name__ == '__main__':
    unittest.main()