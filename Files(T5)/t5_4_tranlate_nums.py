# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import t5_2_file_analyse as t5_2

translator = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять",
    "Ten": "Десять"
}


if __name__ == '__main__':
    data = t5_2.file_analyse('text_files\\numbers_template.txt')
    translated_strings = [f'{translator[el[0]]} {el[1]} {el[2]}\n' for el in data]
    with open('text_files\\t5_4_outfile.tmp.txt', 'w', encoding='utf-8') as outfile:
        outfile.writelines(translated_strings)
