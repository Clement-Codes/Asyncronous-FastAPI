import time
from fastapi import FastAPI
import asyncio

# Create an instance of the FastAPI application
app = FastAPI()

# Endpoint 1(Concurrent): Demonstrates the use of synchronous sleep in an asynchronous function
@app.get("/1")
async def endpoint1():
    print("Hello")
    time.sleep(5)
    print("Bye")

# Endpoint 2(Multi Threading): Proper use of asynchronous sleep in an asynchronous function
@app.get("/2")
async def endpoint2():
    print("Hello")
    await asyncio.sleep(5)
    print("Bye")

# Endpoint 3(Multithreading ): Synchronous endpoint using time.sleep
@app.get("/3")
def endpoint3():
    print("Hello")
    time.sleep(5)
    print("Bye")