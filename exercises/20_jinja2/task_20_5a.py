# -*- coding: utf-8 -*-
"""
Завдання 20.5a

Створити функцію configure_vpn, яка використовує шаблони із завдання 20.5 для
налаштування VPN на маршрутизаторах на основі даних у словнику data.

Параметри функції:
* src_device_params - словник із параметрами підключення до пристрою 1
* dst_device_params - словник із параметрами підключення до пристрою 2
* src_template - ім'я файлу з шаблоном, який створює конфігурацію для 1
* dst_template - ім'я файлу з шаблоном, який створює конфігурацію для 2
* vpn_data_dict - словник зі значеннями, які потрібно підставити в шаблони

Функція повинна налаштувати VPN на основі шаблонів та даних на кожному пристрої
за допомогою Netmiko. Функція повертає кортеж з виведенням команд із двох
маршрутизаторів (результат який повертає метод netmiko send_config_set). Перший
елемент кортежу - виведення з першого пристрою (рядок), другий елемент кортежу
- виведення з другого пристрою.

При цьому у словнику data не вказано номер інтерфейсу Tunnel, який треба
використовувати. Номер треба визначити самостійно з урахуванням інформації з
обладнання. Якщо на маршрутизаторі немає інтерфейсів Tunnel, взяти номер 0,
якщо є - найближчий вільний номер, але однаковий для двох маршрутизаторів.

Наприклад, якщо на маршрутизаторі src такі інтерфейси: Tunnel1, Tunnel4. А на
маршрутизаторі dest такі: Tunnel0, Tunnel2, Tunnel3, Tunnel8. Перший вільний
номер однаковий для двох маршрутизаторів 5. І треба буде налаштувати інтерфейс
Tunnel 5.

Перевірити, які тунельні інтерфейси налаштовані на обладнанні, можна,
наприклад, командою sh ip int br або sh run.

Для цього завдання тест перевіряє роботу функції на перших двох пристроях із
файлу devices.yaml. І перевіряє, що у виведенні є команди налаштування
інтерфейсів, але при цьому не перевіряє налаштовані номери тунелів та інші
команди. Вони мають бути, але тест спрощено.

"""

data = {
    "tun_num": None,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}
