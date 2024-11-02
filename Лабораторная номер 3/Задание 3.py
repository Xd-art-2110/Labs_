# TODO  Напишите функцию count_letters
def count_letters(str):
    letters = []
    for let in str:
        if let.isalpha():
            letters.append(let.lower())
    return letters

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict, a):
    new_dict = {k: v / a for (k, v) in dict.items()}
    return new_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
all_letters = len(count_letters(main_str))
letters = []
for i in range(all_letters):
    if count_letters(main_str)[i] not in letters:
        letters.append(count_letters(main_str)[i])
kol_letters = []
for i in range(len(letters)):
    a = letters[i]
    kol_letters.append(count_letters(main_str).count(a))
dict = dict(zip(letters, kol_letters))
for key, value in calculate_frequency(dict, all_letters).items():
    print(f"{key}: {value:.2f}")
