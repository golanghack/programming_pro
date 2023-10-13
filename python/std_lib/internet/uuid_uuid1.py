#! /usr/bin/env python3 

import uuid

my_uuid = uuid.uuid1()

print(my_uuid)
print(type(my_uuid))
print(f'bytes -> {repr(my_uuid.bytes)}')
print(f'hex -> {my_uuid.hex}')
print(f'int -> {my_uuid.int}')
print(f'urn -> {my_uuid.urn}')
print(f'variant -> {my_uuid.variant}')
print(f'version -> {my_uuid.version}')
print(f'fields -> {my_uuid.fields}')
print(f'time_low -> {my_uuid.time_low}')
print(f'time_mid -> {my_uuid.time_mid}')
print(f'time_hi_version -> {my_uuid.time_hi_version}')
print(f'clock_seq_hi_variant -> {my_uuid.clock_seq_hi_variant}')
print(f'clock_seq_low -> {my_uuid.clock_seq_low}')
print(f'node -> {my_uuid.node}')
print(f'time -> {my_uuid.time}')
print(f'clock_seq -> {my_uuid.clock_seq}')