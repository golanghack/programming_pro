#! /usr/bin/env python3 

import textwrap
import time 

available_clocks = [
    ('monotonic', time.monotonic),
    ('perf_counter', time.perf_counter),
    ('process_time', time.process_time),
    ('time', time.time),
]


for clock_name, func in available_clocks:
    print(textwrap.dedent('''\
        {name}:
        adjustable  -> {info.adjustable}
        implementaion  -> {info.implementation}
        monotonic  -> {info.monotonic}
        resolution  -> {info.resolution}''').format(name=clock_name, 
                                             info=time.get_clock_info(clock_name),
                                             current=func())
          )