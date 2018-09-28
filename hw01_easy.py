__author__ = 'Пашков Игорь Владимирович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

print('Задача-1:')
print('')
number = int(input('Пожалуйста ввелите целое число: '))

while number > 0:
    n = int(number) % 10
    number = int(number) // 10
    print(n)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

print('Задача-2:')
print('')

a = input('Введите число а: ')
b = input('Введите число b: ')

print('С помощью дополнительной переменной:')

x = a
a = b
b = x

print('a: ' + a + ', b: ' + b)
print('')

print('Через арифметические действия: ')
a = int(a)
b = int(b)

a = a + b
b = a - b
a = a - b

print('a: ' + str(a) + ', b: ' + str(b))
print('')

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print('Задача-3:')
print('')

answer = int(input('Укажите свой возраст: '))

if answer >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')