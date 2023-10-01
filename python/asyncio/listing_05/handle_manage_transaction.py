#! /usr/bin/env python3 

import asyncio
import asyncpg

async def main() -> None:
    connection = await asyncpg.connect(host='127.0.0.1', 
                                       port=5432,
                                       database='products', 
                                       user='postgres', 
                                       password='password')
    # transaction
    transaction = connection.transaction()
    await transaction.start()
    try:
        await connection.execute('INSERT INTO brand VALUES(DEFAULT, "brand_1")')
        await connection.execute('INSERT INTO brand VALUES(DEFAULT, "brand_2")')
    except asyncpg.PostgresError:
        print('!!!ERROR!!! Transaction rollback!')
        await transaction.rollback()
    else:
        print('Not Error! Fixing transaction!')
        await transaction.commit()
        
    query = """SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)
    print(brands)
    
    await connection.close()
    
if __name__ == '__main__':
    asyncio.run(main())