import asyncio
import time
import aiohttp

async def fetch_data():
    """Simulates an I/O-bound task (e.g., network request)"""
    print("Fetching data from API...")
    await asyncio.sleep(3)  # Simulates waiting for API response
    print("Data fetched!")

def count_numeros():
    """Simulates a CPU-bound task running while waiting for I/O""" 
    for i in range(1, 10):
        time.sleep(0.5)
        print(f"Counting: {i}")

async def count_numbers():
    """Simulates a CPU-bound task running while waiting for I/O"""
    for i in range(1, 6):
        await asyncio.sleep(0.5)  # Simulates work (non-blocking)
        print(f"Counting: {i}")

async def main():
    # Start both tasks concurrently
    task1 = asyncio.create_task(fetch_data())
    # task2 = asyncio.create_task(count_numbers())
    task2 = asyncio.to_thread(count_numeros)

    await task2
    # Wait for both tasks to complete
    await task1

asyncio.run(main())
