def func_task_3(n):
    """
    Простые делители числа 13195 - это 5, 7, 13 и 29.

    Каков самый большой делитель числа 600851475143, являющийся простым числом?
    """
    divider, result = 2, False
    while n > 1:
        if n % divider == 0:
            n /= divider
            for x in range(2, divider):
                if divider % x == 0:
                    break
            else:
                result = divider
        divider += 1

    return result


# Ниже приведены тесты
import unittest


class TestTask3(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_3(13195), 29)

    def test_task(self):
        self.assertEqual(func_task_3(600851475143), 6857)


if __name__ == '__main__':
    unittest.main()