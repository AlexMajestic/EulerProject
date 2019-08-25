def func_task_1(n):
    """
    Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
    Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
    """
    return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])


# Ниже приведены тесты
import unittest


class TestTask1(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_1(10), 23)

    def test_task(self):
        self.assertEqual(func_task_1(1000), 233168)


if __name__ == '__main__':
    unittest.main()