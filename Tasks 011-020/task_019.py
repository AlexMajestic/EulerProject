import datetime


def func_task_19():
    """
    Дана следующая информация (однако, вы можете проверить ее самостоятельно):

    1 января 1900 года - понедельник.
    В апреле, июне, сентябре и ноябре 30 дней.
    В феврале 28 дней, в високосный год - 29.
    В остальных месяцах по 31 дню.
    Високосный год - любой год, делящийся нацело на 4,
    однако последний год века (ХХ00) является високосным в том и только том случае, если делится на 400.

    Сколько воскресений выпадает на первое число месяца в двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?
    """
    start = datetime.datetime(year=1901, month=1, day=1)
    finish = datetime.datetime(year=2000, month=12, day=31)

    counter = 0
    while start < finish:
        if start.weekday() == 6:
            counter += 1

        next_year = start.year
        next_month = start.month + 1

        if next_month > 12:
            next_year += 1
            next_month = 1
        start = datetime.datetime(year=next_year, month=next_month, day=1)

    return counter


# Ниже приведены тесты
import unittest


class TestTask19(unittest.TestCase):
    def test_task(self):
        self.assertEqual(func_task_19(), 171)


if __name__ == '__main__':
    unittest.main()