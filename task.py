import asyncio  
import time

async def compute(x, y):  
    print("Compute {} + {}...".format(x, y))
    await asyncio.sleep(3.0)
    return x+y

async def print_sum(x, y):  
    result = await compute(x, y)
    print("{} + {} = {}".format(x, y, result))
start = time.time()  
loop = asyncio.get_event_loop()  
tasks = [  
    asyncio.ensure_future(print_sum(0, 0)),
    asyncio.ensure_future(print_sum(1, 1)),
    asyncio.ensure_future(print_sum(2, 2)),
]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()  
print("Total elapsed time {}".format(time.time() - start))
