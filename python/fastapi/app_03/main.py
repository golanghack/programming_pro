from fastapi import FastAPI, Path, Query
from typing import Optional
app = FastAPI()

@app.get('/')
async def index():
    return {'one': 'Hello'}

@app.get('/user/{name}/from/{from_id}')
async def user(from_id: int,
                name: str=Path(None, 
                    title='Name of user',
                    description='Length not more 10 chars',
                    alias='UserName',
                    min_length=5,
                    max_length=15),
                last_name:str=Query(None, 
                    include_in_schema=False,
                    min_length=5, 
                    max_lenght=10),
                age: Optional[int] = None) -> dict:
    my_user = {'name': name, 
                'age': age, 
                'last_name': last_name, 
                'from_id': from_id}
    return my_user

