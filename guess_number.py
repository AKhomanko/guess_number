# Импорт функции получения случайных чисел
# из модуля random.
from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print('Угадайте число от 1 до 100')
amount_tries = 0
while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    guess = int(input('Введите число: '))

    # Если число меньше загаданного...
    if guess < number:
        # ...выводим сообщение.
        print('Ваше число меньше того, что загадано.')
        amount_tries += 1

    # Если число больше загаданного...
    elif guess > number:
        # ...выводим сообщение.
        print('Ваше число больше того, что загадано.')
        amount_tries += 1

    # Если число угадано...
    elif guess == number:
        # ...прерываем выполнение программы и...
        amount_tries += 1
        break
# ...выводим сообщение.
print(f'Отличная интуиция! Вы угадали число за: {amount_tries} попыток)')
