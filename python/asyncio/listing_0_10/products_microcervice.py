#! /usr/bin/env python3 

import functools
from aiohttp import web
from aiohttp.web_request import Request 
from aiohttp.web_response import Response
from create_and_destroy_pool import DB_KEY, create_database_pool, destroy_database_pool

routes = web.RouteTableDef()

@routes.get('/products')
async def products(request: Request) -> Response:
    db = request.app[DB_KEY]
    product_query = 'select product_id, product_name from product'
    result = await db.fetch(product_query)
    return web.json_response([dict(record) for record in result])

app = web.Application()
app.on_startup.append(functools.partial(create_database_pool, 
                                        host='127.0.0.1', 
                                        port=5432, 
                                        user='user_one', 
                                        password='x326y457z', 
                                        database='products'))
app.on_cleanup.append(destroy_database_pool)
app.add_routes(routes)
web.run_app(app, port=8000)