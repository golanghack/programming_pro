#! /usr/bin/env python3 

import pinject

injector = pinject.new_object_graph()

class FakeConnection:
    pass

class FakeBindingSpec(pinject.BindingSpec):
    
    def provide_connection(self):
        return FakeConnection()
    
faked_injector = pinject.new_object_graph(binding_specs=[FakeBindingSpec()])
    