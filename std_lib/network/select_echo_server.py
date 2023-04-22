#! /usr/bin/env python3 

import select
import socket
import sys 
import queue

# cfreate TCP/IP 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# glue socket for port 
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

# listen connections 
server.listen(5)

# waiting read
inputs = [server]

# writing 
outputs = []

# queue for message 
message_queue = {}

while inputs:
    # wait while min 1 socket will be ready 
    print('waiting for the next event', file=sys.stderr)
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server:
            # reading socket is ready for take onnection
            connection, client_address = s.accept()
            print('connection from', client_address, file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            # queue
            message_queue[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # reading client socket have data for read 
                print(f'received {data!r} from {s.getpeername()}', file=sys.stderr,)
                message_queue[s].put(data)
                # add output canak for send answer
                if s not in outputs:
                    outputs.append(s)

                else:
                    # empty result as connection close
                    print('closing', client_address, file=sys.stderr)
                    # break listen connection canal for this connection
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()

                    # remove queue messages
                    del message_queue[s]

    for s in writeable:
        try:
            next_message = message_queue[s].get_nowait()
        except queue.Empty:
            # not have messages wait break testing wriable
            print('  ', s.getpeername(), 'queue empty', file=sys.stderr)
            outputs.remove(s)
        else:
            print(f'sending {next_message!r} to {s.getpeername()}', file=sys.stderr)
    
    for s in exceptional:
        print('exception condition on', s.getpeername(), file=sys.stderr)
        # break listen connection canal for this connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queue[s]
