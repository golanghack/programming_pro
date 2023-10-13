#! /usr/bin/env python3 

import asyncio
import asyncpg

async def main() -> None:
    connection = await asyncpg.connect(host='127.0.0.1', 
                                       port=5432, 
                                       user='postgres', 
                                       database='products', 
                                       password='password')
    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)
    await connection.close()
    
if __name__ == '__main__':
    asyncio.run(main())