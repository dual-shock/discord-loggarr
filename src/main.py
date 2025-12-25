import asyncio
import uvicorn
from src.config import Config
from src.api.application import start
from src.bot.bot import Client

async def start_container():
    Config.check()

    queue = asyncio.Queue()

    api_app = start()
    api_app.state.queue = queue

    client = Client(queue)

    config = uvicorn.Config(
        app=api_app,
        host="0.0.0.0",
        port=8080,
        log_level="debug",
        loop="asyncio",
    )
    server = uvicorn.Server(config)

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(server.serve())
            tg.create_task(client.start(Config.DISCORD_TOKEN))
    except ExceptionGroup as eg:
        # Iterate through all exceptions in the group
        for exc in eg.exceptions:
            print(f"Unhandled error: {type(exc).__name__}: {exc}")

if __name__ == "__main__":
    try:
        asyncio.run(start_container())
    except KeyboardInterrupt:
        print("INFO: User shut down container")
    except Exception as e:
        print(f"ERROR: Container failed to start: {e}")







