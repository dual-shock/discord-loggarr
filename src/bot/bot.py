import discord
import asyncio
import json 
from src.config import Config

intents = discord.Intents.default()


class Client(discord.Client):
    def __init__(self, queue: asyncio.Queue):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.queue = queue
        self.discord_logs_channel_id = Config.DISCORD_LOGS_CHANNEL_ID
    
    async def on_ready(self):
        print(f"INFO: Bot started, logged in as {self.user} (ID: {self.user.id})")
        self.loop.create_task(self.process_webhooks_queue())
    
    async def process_webhooks_queue(self):

        while True: 
            try: 
                data = await self.queue.get()
                print(f"INFO: Processing webhook data: {data}")
                await self.send_webhook_data(data)
            except Exception as e:
                print(f"ERROR: Client.process_webhooks_queue() Failed to process webhook data: {e}")
            finally:
                self.queue.task_done()
    
    async def send_webhook_data(self, data):
        try:
            channel = self.get_channel(int(self.discord_logs_channel_id))

            content = await self.data_to_content(data)
            await channel.send(content)
        except discord.HTTPException as e:
            print(f"ERROR: Client.send_webhook_data() Failed to send message to Discord channel: {e}")
        except Exception as e:
            print(f"ERROR: Client.send_webhook_data() Unexpected error: {e}")
    
    async def data_to_content(self, data):
        if isinstance(data, dict):
            content = json.dumps(data, indent=2)
        else:
            content = str(data)
        
        # Discord has 2000 char limit
        if len(content) > 1900:
            content = content[:1900] + "…"
        
        return f"```json\nnote: im still a useless angel...\n\n{content}\n```"



