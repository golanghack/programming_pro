from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.get('/admin/{name}/branch/{branch_id}')
async def get_admin(branch_id: int=Path(1, gt=0, le=100), 
                    age: int=Query(None, ge=20, lt=61), 
                    name: str=Path(None, min_lenght=10),
                    branch_name: str=Query(None, min_length=5, max_length=10)):
            admin = {'name': name, 'branch': branch_name, 
                        'branch id': branch_id, 'age': age}
            return admin