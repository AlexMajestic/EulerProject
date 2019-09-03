from collections import defaultdict


def func_task_14(n):
    """
    Следующая повторяющаяся последовательность определена для множества натуральных чисел:

    n → n/2 (n - четное)
    n → 3n + 1 (n - нечетное)

    Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов.
    Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается,
    что все сгенерированные таким образом последовательности оканчиваются на 1.

    Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

    Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.
    """

    maximum_row = maximum_start = 0
    passed_ways = defaultdict(int)

    for num in range(2, n):
        result = num
        counter = 0

        while result > 1:
            if result % 2 == 0:
                result = result / 2
                counter += 1
            else:
                result = (3 * result + 1) / 2
                counter += 2

            if result in passed_ways:
                counter += passed_ways[result]
                break

        passed_ways[num] = counter

        if counter > maximum_row:
            maximum_row = counter
            maximum_start = num

    return maximum_start


# Ниже приведены тесты
import unittest


class TestTask14(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_14(10), 9)

    def test_task(self):
        self.assertEqual(func_task_14(1000000), 837799)


if __name__ == '__main__':
    unittest.main()