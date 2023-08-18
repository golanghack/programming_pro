#! /usr/bin/env python3 

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
import datetime


class ExampleService:

    def ping(self):
        """Simple function work with call connect.""" 

        return True

    def now(self):
        """Return current date and time server.""" 

        return datetime.datetime.now()

    def show_type(self, arg):
        """Show send type in server methods.

        Get arg Any type. return tuple with string view.
        """ 

        return (str(arg), str(type(arg)), arg)


    def raises_exception(self, message):
        """Always RuntimeError Exception raise with message"""

        raise RuntimeError(message)

    def send_back_binary(self, bin_):
        """Get one binary arg which unpacked for return."""

        data = bin_.data 
        print(f'send_back_binary({data!r})')
        response = Binary(data)
        return response

if __name__ == '__main__':
    server = SimpleXMLRPCServer(('localhost', 9000), 
                            logRequests=True, 
                            allow_none=True)
    server.register_introspection_functions()
    server.register_multicall_functions()
    server.register_instance(ExampleService())

    try:
        print('Use Cntr-C to exit')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')