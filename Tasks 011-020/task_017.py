def func_task_17(n):
    """
    Если записать числа от 1 до 5 английскими словами (one, two, three, four, five),
    то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.

    Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?


    Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв,
    число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам
    британского английского.
    """
    result = 0
    for i in range(1, n + 1):
        result += number_to_string(i)

    return result


def number_to_string(n):
    str_nums = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }
    str_hundred_nums = {
        0: 'hundred',
        1: 'hundreds'
    }
    str_major_groups = {
        1: {
            0: 'thousand',
            1: 'thousands'
        }
    }

    nums_groups = []
    while n > 0:
        nums_groups.append(n % 1000)
        n //= 1000

    parts = []
    for group in nums_groups:
        if len(str(group)) < 3:
            parts.append([group])
        else:
            parts.append([group - group % 100, group % 100])

    result = ''
    for index, part in enumerate(parts):
        if part[0] == 0:
            continue

        if len(part) == 1:
            if part[0] >= 100:
                result += str_nums[part[0] // 100]
                if part[0] > 100:
                    result += str_hundred_nums[1]
                else:
                    result += str_hundred_nums[0]
            else:
                if len(parts) > 1 and index == 0:
                    result += 'and'

                if 1 <= part[0] < 20:
                    result += str_nums[part[0]]
                else:
                    result += str_nums[part[0] - part[0] % 10]
                    if part[0] % 10 > 0:
                        result += str_nums[part[0] % 10]
        else:
            result += str_nums[part[0] // 100]
            if part[0] > 100:
                result += str_hundred_nums[1]
            else:
                result += str_hundred_nums[0]

            if part[1] == 0:
                continue

            result += 'and'

            if 1 <= part[1] < 20:
                result += str_nums[part[1]]
            else:
                result += str_nums[part[1] - part[1] % 10]
                if part[1] % 10 > 0:
                    result += str_nums[part[1] % 10]

        if index > 0:
            if len(part) == 1:
                if part[0] > 1:
                    result += str_major_groups[index][1]
                else:
                    result += str_major_groups[index][0]
            else:
                result += str_major_groups[index][1]

    return len(result)


# Ниже приведены тесты
import unittest


class TestTask17(unittest.TestCase):
    def test_short(self):
        self.assertEqual(func_task_17(5), 19)

    def test_task(self):
        self.assertEqual(func_task_17(1000), 21924)


if __name__ == '__main__':
    unittest.main()