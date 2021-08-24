# demo-07, event loop demo

import asyncio  
import time


async def compute(x, y):  
    # coroutine is running
    print("Compute {} + {}...".format(x, y))
    # coroutine is suspended here
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):  
    result = await compute(x, y)
    print("{} + {} = {}".format(x, y, result))
    
start = time.time()  

loop = asyncio.get_event_loop() 

# create task object, which is the execute unit in the async context, registered into the event loop.
tasks = [
    asyncio.ensure_future(print_sum(0, 0)), 
    asyncio.ensure_future(print_sum(1, 1)),
    asyncio.ensure_future(print_sum(2, 2)),
]

loop.run_until_complete(asyncio.wait(tasks))  

loop.close()  

print("Total elapsed time {} s".format(time.time() - start))
