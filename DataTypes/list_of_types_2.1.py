# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list_of_types = [5, 5.5, 5 + 8j,
                 "str",
                 [1, "list"],
                 (2.5, "tuple"),
                 {7 + 6j, "set"},
                 frozenset("frozenset"),
                 {15: "dict"},
                 True,
                 bytes("bytes", encoding='utf-8'),
                 bytearray("bytearray", encoding='utf-8'),
                 None,
                 int  # Тип тоже тип
                 ]

for i in list_of_types:
    print(type(i))
