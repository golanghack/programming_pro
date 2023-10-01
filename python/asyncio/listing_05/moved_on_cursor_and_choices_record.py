#! /usr/bin/env python3 

import asyncio
import asyncpg

async def main() -> None:
    connection = await asyncpg.connect(host='127.0.0.1', 
                                       port=5432, 
                                       user='postgres',
                                       database='products',
                                       password='password')
    async with connection.transaction():
        query = 'SELECT product_id, product_name FROM product'
        # create cursor 
        cursor = await connection.cursor(query)
        # moved cursor to front on 500 records
        await cursor.forward(500)
        # get next 100 records
        products = await cursor.fetch(100)
        
        for product in products:
            print(product)
            
    await connection.close()
    
if __name__ == '__main__':
    asyncio.run(main())