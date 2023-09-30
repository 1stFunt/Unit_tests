import pytest
from Homework_6 import ListComparator


def test_calculate_average():  # Тест для проверки правильности расчета среднего значения
    comparator = ListComparator([1, 2, 3, 4, 5], [10, 20, 30])
    assert comparator.calculate_average(comparator.list1) == 3.0
    assert comparator.calculate_average(comparator.list2) == 20.0


def test_compare_average():  # Тесты для сравнения средних значений списков
    # Первый список имеет большее среднее значение
    comparator1 = ListComparator([10, 20, 30], [1, 2, 3, 4, 5])
    assert comparator1.compare_average() == "Первый список имеет большее среднее значение"

    # Второй список имеет большее среднее значение
    comparator2 = ListComparator([1, 2, 3], [10, 20, 30, 40, 50])
    assert comparator2.compare_average() == "Второй список имеет большее среднее значение"

    # Средние значения равны
    comparator3 = ListComparator([1, 2, 3, 4], [1, 2, 3, 4])
    assert comparator3.compare_average() == "Средние значения равны"


def test_empty_lists():  # Тест для случая пустых списков
    comparator = ListComparator([], [])
    assert comparator.compare_average() == "Средние значения равны"


def test_one_empty_list():  # Тест для случая одного пустого списка
    comparator = ListComparator([], [10, 20, 30])
    assert comparator.compare_average() == "Второй список имеет большее среднее значение"


def test_negative_numbers():  # Тест для случая списков с отрицательными числами
    comparator = ListComparator([-1, -2, -3], [-10, -20, -30])
    assert comparator.compare_average() == "Первый список имеет большее среднее значение"


def test_invalid_input():  # Тест для проверки обработки ошибки TypeError при невалидных данных
    list1 = [1, 2, 3, '4']  # '4' - это строка, а не число
    list2 = [10, 20, 30, 40]
    with pytest.raises(TypeError) as e:
        comparator = ListComparator(list1, list2)
        comparator.validate_lists()
    assert str(e.value) == "Все элементы списка должны быть числами."


if __name__ == '__main__':
    pytest.main()
