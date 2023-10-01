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
    async with connection.transaction():
        await connection.execute('INSERT INTO brand VALUES(DEFAULT, "my_new_brand")')
        
        try:
            async with connection.transaction():
                await connection.execute('INSERT INTO product_color VALUES(1, "black")')
        except Exception as err:
            logging.warning('ERROR with inserting color name  ignore', exc_info=err)
    await connection.close()
    
if __name__ == '__main__':
    asyncio.run(main())