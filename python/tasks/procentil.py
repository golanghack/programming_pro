#! /usr/bin/env python3 


"""<--PROENTIL-->"""
"""<-TASK TEXT->"""
""" 
Представьте, что вы открыли в банке сберегательный счет под 4 % годо-
вых. Проценты банк рассчитывает в конце года и добавляет к сумме счета.
Напишите программу, которая запрашивает у пользователя сумму перво-
начального депозита, после чего рассчитывает и выводит на экран сумму
на счету в конце первого, второго и третьего годов. Все суммы должны
быть округлены до двух знаков после запятой.
"""

year_proc: float = 0.04

try: 
    message = 'Enter summ -> '
    line = input(message)
    deposit = int(line)
    years = (1, 2, 3)
    on_summ = deposit + ((deposit * year_proc) * years[0]) 
    two_summ = deposit + ((deposit * year_proc) * years[1])
    three_summ = deposit + ((deposit * year_proc) * years[2])
    
    print(f'summ from deposit after one year -> {on_summ:.2f}')
    print(f'summ from deposit after two years -> {two_summ:.2f}')
    print(f'summ form deposit after three year -> {three_summ:.2f}')
except ValueError as err:
    print(f'!!!ERROR!!! -> {err} -> Used this program again, please!')