# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('text_files\\t5_5_outfile.tmp.txt', 'w+', encoding='utf-8') as io_file:
    io_file.write(' '.join([str(randint(0, 1000)) for _ in range(100)]))
    io_file.seek(0)
    print(sum(map(int, io_file.readline().split())))
