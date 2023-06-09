# -*- coding: utf-8 -*-

"""
Завдання 22.1

Створити клас Topology, який представляє топологію мережі.

При створенні екземпляра класу як аргумент передається словник, який описує
топологію. Словник може містити "дублюючі" з'єднання. Тут "дублюючі"
з'єднання, це ситуація коли в словнику є два з'єднання:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Завдання залишити лише одне з цих з'єднань у підсумковому словнику, не важливо яке.

У кожному екземплярі має бути створена змінна topology, в якій міститься
словник топології, але вже без "дублів". Змінна topology повинна містити
словник без "дублів" відразу після створення екземпляра.

Приклад створення екземпляра класу:

In [2]: top = Topology(topology_example)

Після цього, повинна бути доступна змінна topology:

In [3]: top.topology
Out[3]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

"""

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}
