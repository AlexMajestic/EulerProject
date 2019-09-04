def func_task_15(n):
    """
    Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
    существует ровно 6 маршрутов до правого нижнего угла сетки.

    Сколько существует таких маршрутов в сетке 20×20?
    """

    trianle = []
    max_size = 2 * n + 1

    for i in range(max_size):
        row = []
        for j in range(max_size):
            row += [0]
        trianle.append(row)

    trianle[0][0] = 1
    trianle[1][0] = trianle[1][1] = 1

    for i in range(2, max_size):
        for j in range(i + 1):
            if j == 0:
                trianle[i][j] = trianle[i - 1][j]
            elif j == i:
                trianle[i][j] = trianle[i - 1][j - 1]
            else:
                trianle[i][j] = trianle[i - 1][j - 1] + trianle[i - 1][j]

    return max(trianle[max_size - 1])


# Ниже приведены тесты
import unittest


class TestTask15(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_15(2), 6)

    def test_task(self):
        self.assertEqual(func_task_15(20), 137846528820)


if __name__ == '__main__':
    unittest.main()