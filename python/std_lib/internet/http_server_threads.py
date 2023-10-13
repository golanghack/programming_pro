#! /usr/bin/env python3 

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message.encode('utf-8'))
        self.wfile.write(b'\n')


class ThreadHTTPServer(ThreadingMixIn, HTTPServer):
    """Work with requests in different thread"""


if __name__ == '__main__':
    server = ThreadHTTPServer(('localhost', 8082), Handler)
    print('Starting Server, use <Ctrl-C> to stop')
    server.serve_forever()