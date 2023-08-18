#! /usr/bin/env python3 

import io 
import mimetypes
from urllib import request
import uuid

class MultiPartForm:
    """Accommulation data for publication in form."""

    def __init__(self):
        self.form_fields = []
        self.files = []

        # use sporadic bite string long lenght 
        # for different parts MIME data 
        self.boundary = uuid.uuid4().hex.encode('utf-8')
        return

    def get_content_type(self):
        return f'multipart/form-data -> boundary={self.boundary.decode('utf-8')}'

    def add_field(self, name, value):
        """Added simple field im form."""
        self.form_fields.append((name, value))

    def add_file(self, fieldname, filename, file_handle, mimetype=None):
        """Added download file."""

        body = file_handle.read()
        if mimetype is None:
            mimetype = (
                mimetypes.guess_type(filename)[0] or 
                    'application/octet-stream'
            )
        self.files.append((fieldname, filename, mimetype, body))
        return

    @staticmethod
    def _form_data(name):
        return ('Content-Disposition: form-data; ', 
                    f'name="{name.encode('utf-8')}"\r\n')
    
    @staticmethod
    def _attached_file(name, filename):
        return ('Content-Dosposition -> file; '
                    f'name = "{(name, filename).encode('utf-8')}"')

    @staticmethod
    def _content_type(ct):
        return f'Content-Type: {(ct).encode('utf-8')}\r\n'

    def __bytes__(self):
        """Return bites string for form with files."""

        buffer = io.BytesIO()
        boundary = b'--' + self.boundary + b'\r\n'

        # added fields of form
        for name, value in self.form_fields:
            buffer.write(boundary)
            buffer.write(self._form_data(name))
            buffer.write(b'\r\n')
            buffer.write(value.encode('utf-8'))
            buffer.write(b'\r\n')

        # added download files
        for f_name, filename, f_content_type, body in self.files:
            buffer.write(boundary)
            buffer.write(self._attached_file(name, filename))
            buffer.write(self._content_type(f_content_type))
            buffer.write(b'\r\n')
            buffer.write(body)
            buffer.write(b'\r\n')

        buffer.write(b'--' + self.boundary + b'--\r\n')
        return buffer.getvalue()

if __name__ == '__main__':
    # crrate form with simple fields 
    form = MultiPartForm()
    form.add_field('first_name', 'Golang')
    form.add_field('last_name', 'Hack')

    # addef fictive file 
    form.add_file(
        'biography', 'bio.txt', 
        file_handle=io.BytesIO(b'Pythom developer and blogger')
    )
    # create request with bite string for file
    data = bytes(form)
    req = request.Request('https://localhost:8080/', data=data)
    req.add_header('User_agent', 'Nasa (https://nasa.gov/)',)
    req.add_header('Content-Type', form.get_content_type())
    req.add_header('Content-length', len(data))

    print()
    print('Out -> ')
    for name, value in req.header_items():
        print(f'{name} -> {value}')
    print()
    print(req.data.decode('utf-8'))

    print()
    print('Server response')
    print(request.urlopen(req).read().decode('utf-8'))
    