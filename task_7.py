def func_task_7(n):
    """
    Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

    Какое число является 10001-ым простым числом?
    """
    counter = num = 1
    simple = [2]
    while counter < n:
        num += 2
        for i in simple:
            if num % i == 0:
                break
        else:
            counter += 1
            simple.append(num)

    return num


# Ниже приведены тесты
import unittest


class TestTask4(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_7(6), 13)

    def test_middle(self):
        self.assertEqual(func_task_7(500), 3571)

    def test_task(self):
        self.assertEqual(func_task_7(10001), 104743)


if __name__ == '__main__':
    unittest.main()