#! /usr/bin/env python3 

import asyncio
from asyncio import StreamReader, StreamWriter
from API_file_upload_to_server import FileUpload

class FileServer:
    
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.upload_event = asyncio.Event()
        
    async def start_server(self):
        server = await asyncio.start_server(self._client_connected, 
                                            self.host, 
                                            self.port)
        await server.serve_forever()
        
    async def dump_contents_on_complete(self, upload: FileUpload):
        file_contents = await upload.get_contents()
        print(file_contents)
        
    def _client_connected(self, reader: StreamReader, 
                          writer: StreamWriter):
        upload = FileUpload(reader, writer)
        upload.listen_for_uploads()
        asyncio.create_task(self.dump_contents_on_complete(upload))
        
async def main():
    server = FileServer('127.0.0.1', 8000)
    await server.start_server()
    
asyncio.run(main())
 