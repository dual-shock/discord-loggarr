import os
from dotenv import load_dotenv

load_dotenv()

class Config: 
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    DISCORD_LOGS_CHANNEL_ID = os.getenv("DISCORD_LOGS_CHANNEL_ID")
    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

    @classmethod
    def exists(cls, env_var: str):
        value = os.getenv(env_var)
        if not value: 
            print(f"ERROR: {env_var} not set either in .env config file or environment")
        return value

    @classmethod
    def check(cls):
        if not cls.DISCORD_TOKEN:
            print("ERROR: DISCORD_TOKEN not set in .env")
        else: print(f"INFO: DISCORD_TOKEN found: {cls.DISCORD_TOKEN[:4]}****")
        if not cls.DISCORD_LOGS_CHANNEL_ID:
            print("ERROR: DISCORD_LOGS_CHANNEL_ID not set in .env")
        else: print(f"INFO: DISCORD_LOGS_CHANNEL_ID found: {cls.DISCORD_LOGS_CHANNEL_ID}")
        if not cls.WEBHOOK_SECRET:
            print("WARNING: optional WEBHOOK_SECRET not set in .env, webhooks will not be secured")
        else: print(f"INFO: WEBHOOK_SECRET found: {cls.WEBHOOK_SECRET[:4]}****")

# config = Config()
# config.check()