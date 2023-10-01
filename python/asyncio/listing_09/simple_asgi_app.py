#! /usr/bin/env python3


async def app(scope, recieve, send):
    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"text/html"]],
        }
    )

    await send({"type": "http.response.body", "body": b"ASGI"})
