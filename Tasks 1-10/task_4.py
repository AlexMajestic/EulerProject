def func_task_4(n):
    """
    Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
    Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

    Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
    """
    maximum = 0
    for a in range(10 ** n, 10 ** (n - 1), -1):
        for b in range(a, 10 ** (n - 1), -1):
            result = a * b

            if result < maximum:
                break

            if str(result) == str(result)[::-1] and result > maximum:
                maximum = result

    return maximum


# Ниже приведены тесты
import unittest


class TestTask4(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_4(2), 9009)

    def test_task(self):
        self.assertEqual(func_task_4(3), 906609)


if __name__ == '__main__':
    unittest.main()