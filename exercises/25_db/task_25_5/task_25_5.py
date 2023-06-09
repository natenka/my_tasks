# -*- coding: utf-8 -*-
"""
Завдання 25.5

Для завдань 25 розділу немає тестів!

Після виконання завдань 25.1 – 25.5 у БД залишається інформація про неактивні
записи.  І, якщо якась MAC-адреса не з'являлася у нових записах, запис із нею,
може залишитися у БД назавжди.

І хоча це може бути корисно, щоб подивитися, де MAC-адреса знаходилася в
останній раз, постійно зберігати цю інформацію не дуже корисно.
Наприклад, якщо запис у БД вже більше місяця, то його можна видалити.

Щоб зробити такий критерій, потрібно ввести нове поле, в яке буде записуватися
час додавання запису.

Нове поле називається last_active і в ньому має бути рядок, у форматі:
YYYY-MM-DD HH:MM:SS.  У цьому завданні необхідно:
* Змінити, відповідно, таблицю dhcp і додати нове поле.
  Таблицю можна змінити з cli sqlite
* змінити скрипт add_data.py, щоб він додав до кожного запису час

Отримати рядок з часом і датою у зазначеному форматі можна за допомогою функції
datetime у запиті SQL.

Синтаксис використання такий:
sqlite> insert into dhcp (mac, ip, vlan, interface, switch, active, last_active)
   ...> values ('00:09:BC:3F:A6:50', '192.168.100.100', '1', 'FastEthernet0/7', 'sw1', '0', datetime('now'));

Тобто замість значення, яке записується до бази даних, треба вказати
datetime('now').

Після цієї команди у базі даних з'явиться такий запис:
mac                ip               vlan  interface        switch  active  last_active
-----------------  ---------------  ----  ---------------  ------  ------  -------------------
00:09:BC:3F:A6:50  192.168.100.100  1     FastEthernet0/7  sw1     0       2019-03-08 11:26:56
"""
