# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

var1 = 0
var2 = '42'
var3 = -42.0

print(f'var1 = {var1} has type {type(var1)}\n'
      f'var2 = {var2} has type {type(var2)}\n'
      f'var3 = {var3} has type {type(var3)}\n'
      )

var1 = int(input('Input integer: '))
var2 = input('input string: ')
var3 = float(input('input float: '))

print(f'var1 = {var1} has type {type(var1)}\n'
      f'var2 = {var2} has type {type(var2)}\n'
      f'var3 = {var3} has type {type(var3)}\n'
      )
