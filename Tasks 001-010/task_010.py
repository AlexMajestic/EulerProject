def func_task_10(n):
    """
    Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

    Найдите сумму всех простых чисел меньше двух миллионов.
    """
    simple = list(range(n + 1))
    simple[1] = 0
    for i in simple:
        if i > 1:
            for j in range(i + i, len(simple), i):
                simple[j] = 0
    return sum(simple)

# Ниже приведены тесты
import unittest


class TestTask7(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_10(10), 17)

    def test_task(self):
        self.assertEqual(func_task_10(2000000), 142913828922)


if __name__ == '__main__':
    unittest.main()