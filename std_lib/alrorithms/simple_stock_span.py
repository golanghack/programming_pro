#! /usr/bin/env python3 

""" 
Simple algorithm for task different courses
""" 

def simple_stock_span(quotes: list) -> list:
    """Return list spans with diffrenet courses"""

    spans = [i for i in range(8)]
    for i in quotes:
        different_number = 1
        span_end_switcher = False
        while i - different_number >= 0 and span_end_switcher:
            if quotes[i - different_number] <= quotes[i]:
                different_number = different_number + 1
            else:
                span_end_switcher = True
        spans[i] = different_number
    return spans 

simple_list = [1, 2, 4, 3, 1, 6]

print(simple_stock_span(simple_list))