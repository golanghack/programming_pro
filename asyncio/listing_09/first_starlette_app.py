#! /usr/bin/env python3

import asyncpg
from asyncpg import Record
from asyncpg.pool import Pool
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.routing import Route
from typing import List, Dict


async def create_database_pool():
    pool: Pool = await asyncpg.create_pool(
        host="127.0.0.1",
        port=5432,
        user="user_one",
        database="products",
        password="x326y457z",
        min_size=6,
        max_size=6,
    )
    app.state.DB = pool


async def destroy_database_pool():
    pool = app.state.DB
    await pool.close()


async def brands(request: Request) -> Response:
    connection: Pool = request.app.state.DB

    brand_query = "select brand_id, brand_name from brand"
    results: List[Record] = await connection.fetch(brand_query)
    results_as_dict: List[Dict] = [dict(brand) for brand in results]
    return JSONResponse(results_as_dict)


app = Starlette(
    routes=[Route("/brands", brands)],
    on_startup=[create_database_pool],
    on_shutdown=[destroy_database_pool],
)
