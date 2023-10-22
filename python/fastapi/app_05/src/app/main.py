from fastapi import FastAPI

app = FastAPI()

@app.get('/ping')
async def pong():
    """Return json object with 'pong'"""
    
    return {'ping': 'pong'}