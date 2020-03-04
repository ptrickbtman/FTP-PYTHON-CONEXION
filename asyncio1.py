
#pip install asyncio
import asyncio

async def message(text, s):
    await asyncio.sleep(s)
    print(text)
    
loop = asyncio.get_event_loop()

# first task
loop.create_task(message("Message #1", 2))


# second task
loop.create_task(message("Message #2", 1))

loop.run_forever()
loop.close()




