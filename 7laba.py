#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

if __name__ == '__main__':
    # Список .
    spisoks = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input("Введите команду: ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные .
            name = input("Фамилия, Имя ")
            tel = input("Номер телефона ")
            date = input("Дата рождения ")

            # Создать словарь.
            spisok = {
                'name': name,
                'tel': tel,
                'date': date,
            }

            # Добавить словарь в список.
            spisoks.append(spisok)
            # Отсортировать список в случае необходимости.
            if len(spisok) > 1:
                spisoks.sort(key=lambda item: item.get('tel', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 30,
                '-' * 20,
                '-' * 14
            )
            print(line)
            print(
                '| {:^30} | {:^20} | {:^14} |'.format(
                    "Фамилия, Имя",
                    "Номер телефона",
                    "Дата рождения",
                )
            )
            print(line)

            # Вывести данные о всех людях.
            for idx, product in enumerate(spisoks, 1):
                print(
                    '| {:<30} | {:<20} | {:>14} |'.format(
                        product.get('name', ''),
                        product.get('tel', ''),
                        product.get('date', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = (parts[1])

            count = 0
            for spisok in spisoks:
                if spisok.get('name') == sel:
                    count = "Дата рождения"
                    print(
                        '{:>4}: {}'.format(count, spisok.get('date', ''))
                    )
                    print('Номер телефона', spisok.get('tel', ''))
                    print('Фамилия Имя', spisok.get('name', ''))

            # Если счетчик равен 0, то человек не найден.
            if count == 0:
                print("Люди не найден.")

        elif command.startswith('load'):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Прочитать данные из файла JSON.
            with open('2.json', 'r') as f:
                spisoks = json.load(f)

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Сохранить данные в файл JSON.
            with open('2.json', 'w') as f:
                json.dump(spisoks, f)
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select <товар> - информация о человеке;")
            print("save 'имя файла' - сохранить данные в файл;")
            print("load 'имя файла' - загрузить данные из файла;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("Неизвестная команда {command}", file=sys.stderr)
