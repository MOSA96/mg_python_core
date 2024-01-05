import asyncio

async def arcane_task(magic_source, seconds):
    """An asynchronous coroutine that mimics gathering mystical energy from a source."""
    print(f'Start gathering from {magic_source}.')
    await asyncio.sleep(seconds) 
    print(f'Finished gathering from {magic_source}.')
    return f'Energy from {magic_source}'

async def magical_confluence():
    tasks = [arcane_task("Crystal Shard", 3),
             arcane_task("Ancient Runestone", 2),
             arcane_task("Enchanted Spring", 1)]
    gathered_energies = await asyncio.gather(*tasks)
    print(f"All energies gathered: {', '.join(gathered_energies)}")

asyncio.run(magical_confluence())