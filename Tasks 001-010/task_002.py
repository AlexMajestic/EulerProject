def func_task_2(n):
    """
    Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
    Начиная с 1 и 2, первые 10 элементов будут:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
    """
    result, x, y = 0, 0, 1
    while y < n:
        y, x = x + y, y

        if y % 2 == 0:
            result += y
    return result


# Ниже приведены тесты
import unittest


class TestTask2(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_2(10), 10)

    def test_task(self):
        self.assertEqual(func_task_2(4000000), 4613732)


if __name__ == '__main__':
    unittest.main()