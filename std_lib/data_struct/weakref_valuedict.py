#! /usr/bin/env python3

import gc 
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

class SuperObject:
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self) -> str:
        return f'SuperObject -> {self.name}'
    
    def __del__(self):
        print(f'    (Deleting {self})')
        
def demo(cache_factory):
    """Take objects for realtime deleting weakref."""
    
    all_refs = {}
    
    #cache
    print('CACHE TYPE -> ', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        obj_name = SuperObject(name)
        cache[name] = obj_name
        all_refs[name] = obj_name
        del obj_name # less counter links
        
    print('  all_refs = ', end=' ')
    pprint(all_refs)
    print('\nBefore, cache contains -> ', list(cache.keys()))
    for name, value in cache.items():
        print(f'    {name} = {value}')
        del value # less counter links 
        
    # delete all links on objects on excepting which in cache
    print('\n Clean up ->')
    del all_refs
    gc.collect()
    
    print('\n After, cache contains -> ', list(cache.keys()))
    for name, value in cache.items():
        print(f'    {name} = {value}')
    print('   demo returning')
    return

demo(dict)
print()

demo(weakref.WeakValueDictionary)