#! /usr/bin/env python3 

""" 
Программа, которую вы напишете, должна начинаться с запроса у поль-
зователя суммы заказа в ресторане. После этого должен быть произведен
расчет налога и чаевых официанту. Вы можете использовать принятую
в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве
чаевых мы оставим 18 % от стоимости заказа без учета налога. На выхо-
де программа должна отобразить отдельно налог, сумму чаевых и итог,
включая обе составляющие. Форматируйте вывод таким образом, чтобы
все числа отображались с двумя знаками после запятой.
"""

tax: float = 0.2
comission: float = 0.18

message: str = 'Enter summ for order -> '

try:
    line = input(message)
    summ = int(line)
    tea__from_summ = summ * comission
    tax__from_summ = summ * tax
    after_comission = summ - tea__from_summ
    after_tax = after_comission - (after_comission * tax)
    finish_summ = after_tax
    print(f'tea -> {tea__from_summ:.2f}')
    print(f'Tax -> {tax__from_summ:.2f}')
    print(f'finish summ -> {finish_summ:.2f}')
except ValueError as err:
    print(err)
    