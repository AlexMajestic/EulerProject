from math import sqrt

def func_task_21():
    """
    Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
    Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой,
    а каждое из чисел a и b - дружественным числом.

    Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110,
    поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

    Подсчитайте сумму всех дружественных чисел меньше 10000.
    """
    result = 0
    used_nums = []

    for num in range(6, 10000):
        if num in used_nums:
            continue

        sum1 = -num
        for i in range(1, int(sqrt(num))):
            if num % i == 0:
                sum1 += i + num // i

        sum2 = -sum1
        for i in range(1, int(sqrt(sum1))):
            if sum1 % i == 0:
                sum2 += i + sum1 // i

        if sum2 == num:
            used_nums += [sum2] + [sum1]
            if sum1 == sum2:
                result += sum1
            else:
                result += sum1 + sum2

    return result


# Ниже приведены тесты
import unittest


class TestTask21(unittest.TestCase):
    def test_task(self):
        self.assertEqual(func_task_21(), 40278)


if __name__ == '__main__':
    unittest.main()