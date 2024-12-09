import time
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/1")
async def endpoint1():
    print("Hello")
    time.sleep(5)
    print("Bye")

@app.get("/2")
async def endpoint2():
    print("Hello")
    await asyncio.sleep(5)
    print("Bye")

@app.get("/3")
def endpoint3():
    print("Hello")
    time.sleep(5)
    print("Bye")