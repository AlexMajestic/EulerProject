def func_task_15(n):
    """
    Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
    существует ровно 6 маршрутов до правого нижнего угла сетки.

    Сколько существует таких маршрутов в сетке 20×20?
    """
    n += 1
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    matrix[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[n][n]

# Ниже приведены тесты
import unittest


class TestTask15(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_15(2), 6)

    def test_task(self):
        self.assertEqual(func_task_15(20), 137846528820)


if __name__ == '__main__':
    unittest.main()