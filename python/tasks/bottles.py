#! /usr/bin/env python3 
"""<--BOTTLES-->
<--TASK-->
Во многих странах в стоимость стеклотары закладывается определенный
депозит, чтобы стимулировать покупателей напитков сдавать пустые бу-
тылки. Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутыл-
ки большего объема – $0,25.
Напишите программу, запрашивающую у пользователя количество бу-
тылок каждого размера. На экране должна отобразиться сумма, которую
можно выручить, если сдать всю имеющуюся посуду. Отформатируйте
вывод так, чтобы сумма включала два знака после запятой и дополнялась
слева символом доллара.
"""

small_deposit: float = 0.1
big_deposit: float = 0.25
message_for_big: str = 'Enter count of buttle big -> '
message_for_small: str = 'Enter count of buttle small -> '
try:
    line_big = input(message_for_big)
    line_small = input(message_for_small)
    big: int = int(line_big)
    small: int = int(line_small)
    summ_big = big * big_deposit
    summ_small = small * small_deposit
    full_summ = summ_big + summ_small
    print(f'full summ --> {full_summ:.2f}')
except ValueError as err:
    print(err)

