#! /usr/bin/env python3 

import uuid

namespace_types = sorted(
    n
    for n in dir(uuid) 
    if n.startswith('NAMESPACE_')
)
name = 'nasa.gov'

for namespace_type in namespace_types:
    print(namespace_type) 
    namespace_uuid = getattr(uuid, namespace_type)
    print(f'{uuid.uuid3(namespace_uuid, name)}')
    print(f'{uuid.uuid3(namespace_uuid, name)}')
    print()