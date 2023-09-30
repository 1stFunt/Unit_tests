"""
Создайте программу на Python или Java, которая принимает
два списка чисел и выполняет следующие действия:
a. Рассчитывает среднее значение каждого списка.
b. Сравнивает эти средние значения и выводит соответствующее сообщение:
- ""Первый список имеет большее среднее значение"",
если среднее значение первого списка больше.
- ""Второй список имеет большее среднее значение"",
если среднее значение второго списка больше.
- ""Средние значения равны"", если средние значения списков равны.
"""


class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, numbers):
        if len(numbers) == 0:
            return 0
        return sum(numbers) / len(numbers)

    def compare_average(self):
        avg1 = self.calculate_average(self.list1)
        avg2 = self.calculate_average(self.list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"

    @staticmethod
    def validate_input(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Все элементы списка должны быть числами.")

    def validate_lists(self):
        for num in self.list1 + self.list2:
            self.validate_input(num)


# list1 = [float(x) for x in input(
#     "Введите элементы первого списка через пробел: ").split()]
# list2 = [float(x) for x in input(
#     "Введите элементы второго списка через пробел: ").split()]
# comparator = ListComparator(list1, list2)
# result = comparator.compare_average()
# print(result)
