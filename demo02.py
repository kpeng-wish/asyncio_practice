# demo-02, async version 

import asyncio

async def count(): # define a coroutine
    print("One")
    await asyncio.sleep(1) # any time-intensive processes that involve wait time. must be awaitable
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()

    asyncio.run(main()) # Python 3.7+

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")