#! /usr/bin/env python3 

import asyncpg
import asyncio
from typing import List, Tuple, Union
from random import sample

def load_common_words() -> List[str]:
    """Loading words from files -> common_words.txt saved in this directory."""
    
    with open('common_words.txt') as common_words:
        return common_words.readlines()
    
def generate_brand_names(words: List[str]) -> List[Tuple[Union[str, ]]]:
    """Creating brand name for marks."""
    
    return [(words[index], ) for index in sample(range(100), 100)]

async def insert_brands(common_words, connection) -> int:
    """Inserting generated data in database."""
    
    brands = generate_brand_names(common_words)
    insert_brands = 'INSERT INTO brand VALUES(DEFAULT, $1)'
    return await connection.executemany(insert_brands, brands)

async def main() -> None:
    common_words = load_common_words()
    connection = await asyncpg.connect(host='127.0.0.1', 
                                       port=5432, 
                                       user='postgres', 
                                       database='products', 
                                       password='password')
    await insert_brands(common_words, connection)

if __name__ == '__main__':
    asyncio.run(main())
