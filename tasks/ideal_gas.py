#! /usr/bin/env python3

"""<-IDEAL GAS->

Уравнение состояния идеального газа представляет собой математиче-
скую аппроксимацию поведения газов в условиях изменения давления,
объема и температуры. Обычно соответствующая формула записывается
так:
PV = nRT,
где P – это давление в паскалях, V – объем в литрах, n – количество ве-
щества в молях, R – универсальная газовая постоянная, равная 8,314
Дж/(моль·К), а T – температура по шкале Кельвина.
Напишите программу для измерения количества газа в молях при за-
данных пользователем давлении, объеме и температуре. Проверьте свою
программу путем вычисления количества газа в баллоне для дайвинга.
Типичный баллон вмещает 12 л газа под давлением 20 000 000 Па (при-
мерно 3000 фунтов на кв. дюйм). Температуру в комнате примем за 20°
по шкале Цельсия или 68° по Фаренгейту.
Подсказка. Чтобы перевести температуру из градусов Цельсия в Кельвины, необхо-
димо прибавить к ней 273,15. Из Фаренгейта в Кельвины температура переводится
путем вычитания из нее 32, умножения результата на и прибавления тех же 273,15.
"""

messages: list = [
    'Enter pressure (in Pascales) -> ', 
    'Enter valume (in Litrs) -> ', 
    'Enter temperature (in Kelvin`s)',
    ]

try:
    pressure = int(input(messages[0]))
    valume = int(input(messages[1]))
    temperature = int(input(messages[2]))
except ValueError as err:
    print(f'!!!ERRORR!!! -> {err}.')
    print('Try again!')

KELVIN = 273.15
UNIVERSAL_GAS_CONST = 8.314

ballon_valume: int = 12 
pressure_in_ballon: int = 20_000_000
temperature_in_ballon: float = 20 + KELVIN

standart: float = (pressure_in_ballon * ballon_valume) / (UNIVERSAL_GAS_CONST * temperature_in_ballon)

use_user_data: float = (pressure * valume) / (UNIVERSAL_GAS_CONST * temperature)

print(f'Standart mean for this task -> {standart:.2f}')
print()
print(f'User data mean -> {use_user_data:.2f}')



