#! /usr/bin/env python3 

import asyncpg
from asyncpg.pool import Pool
from aiohttp import web 
from aiohttp.web_app import Application
from aiohttp.web_request import Request 
from aiohttp.web_response import Response

routes = web.RouteTableDef()
DB_KEY = 'database'

async def create_database_pool(app: Application):
    print('Create pool connections')
    pool: Pool = await asyncpg.create_pool(host='127.0.0.1', 
                                           port=5432, 
                                           user='user_one', 
                                           password='x326y457z', 
                                           database='products',
                                           min_size=6,
                                           max_size=6)
    app[DB_KEY] = pool 
    
async def destroy_database_pool(app: Application):
    print('Destroy pool connections.')
    pool: Pool = app[DB_KEY]
    await pool.close()
    
@routes.post('/product')
async def create_product(request: Request) -> Response:
    product_name = 'product_name'
    brand_id = 'brand_id'
    
    if not request.can_read_body:
        raise web.HTTPBadRequest()
    
    body = await request.json()
    
    if product_name in body and brand_id in body:
        db = request.app[DB_KEY]
        await db.execute("""
                         insert into product(product_id, product_name, brand_id)
                         values (default, $1, $2)
                         """, 
                         body[product_name], 
                         int(body[brand_id]))
        return web.Response(status=201)
    
    else:
        raise web.HTTPBadRequest()
app = web.Application()
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app, port=8081)