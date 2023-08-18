#! /usr/bin/env python3

import asyncio 
import asyncpg 
import logging

async def main() -> None:
    connection = await asyncpg.connect(host='127.0.0.1', 
                                       port=5432, 
                                       user='postgres', 
                                       database='products', 
                                       password='password')
    try:
        async with connection.transaction():
            insert_brand = 'INSERT INTO brand VALUES(9999, "big_brand")'
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception:
        logging.exception('Error on transaction!')
    finally:
        query = """SELECT brand_name FROM brand WHERE brand_name LIKE "big_%" """
        # testing trasaction
        brands = await connection.fetch(query)
        print(f'Result request -> {brands}')
        
        await connection.close()
        
if __name__ == '__main__':
    asyncio.run(main())