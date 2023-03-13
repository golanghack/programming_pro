#! /usr/bin/env python3 

import sys 

[sys.stdout.buffer.write(b'Hi\n') for _ in range(1000000)]

sys.stdout.flush()