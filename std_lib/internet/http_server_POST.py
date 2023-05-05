#! /usr/bin/env python3 

import cgi
from http.server import BaseHTTPRequestHandler
import io 


class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # analise
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        # begin answer
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False, 
            write_through=True,
        )

        out.write(f'Client -> {self.client_address}\n')
        out.write(f'User-agent -> {self.headers["user-agent"]}')
        out.write(f'Path -> {self.path}')
        out.write('Form data -> \n')

        # send back to client
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                out.write(
                    f'\tUploaded {field} as {field_item!r} ({file_len}bytes\n)' 
                    )

            else:
                out.write(f'\tUploaded {field} as {field_item!r} ({file_len} bytes)')

        # turn of TextIOWrapper
        out.detach()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8082), PostHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
