#! /usr/bin/env python3 

import pinject
from Connection import Connection

class PrototypeBindingSpec(pinject.BindingSpec):
    
    @pinject.provides(in_scope=pinject.PROTOTYPE)
    def provide_connect(self):
        return Connection(None)
    
proto_injector = pinject.new_object_graph(binding_specs=[PrototypeBindingSpec()])