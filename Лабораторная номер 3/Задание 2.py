# TODO Напишите функцию find_common_participants


def find_common_participants(str1, str2, spltr = ','):
    str1 = str1.split(spltr)
    str2 = str2.split(spltr)
    set_str1 = set(str1)
    set_str2 = set(str2)
    all_str = list(set_str1.intersection(set_str2))
    all_str.sort()
    return all_str

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, spltr='|'))
