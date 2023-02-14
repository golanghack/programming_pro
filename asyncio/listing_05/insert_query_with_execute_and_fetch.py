#! /usr/bin/env python3 

import asyncpg
import asyncio
from typing import List

async def main() -> None:
    connection = await asyncpg.connect(host='127.0.0.1', 
                                       port=5432, 
                                       user='postgres', 
                                       database='products', 
                                       password='password'
                                       )
    await connection.execute('INSERT INTO brand VALUES(DEFAULT, "Levis")')
    await connection.execute('INSERT INTO brand VALUES(DEFAULT, "Seven")')
    
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: List[asyncpg.Record] = await connection.fetch(brand_query)
    
    for brand in results:
        print(f'id -> {brand["brand_id"]}, name -> {brand["brand_name"]}')
    await connection.close()
    
asyncio.run(main())