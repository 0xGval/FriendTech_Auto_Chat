import asyncio
import discord
from discord.ext import commands
import websockets
import json
import logging
from config import API, AUTHORIZATION_TOKEN, DISCORD_BOT_TOKEN, TARGET_CHANNEL_ID
from chat_room_ids import CHAT_ROOM_IDS


# Setting up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIBase:
    def __init__(self) -> None:
        self.session = None

    async def connect(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        self.session = await websockets.connect(f"wss://{API}/?authorization={AUTHORIZATION_TOKEN}", extra_headers=headers)

    async def disconnect(self):
        if self.session:
            await self.session.close()
            self.session = None

class NonRest:
    def __init__(self, api_base: APIBase):
        self.api_base = api_base

    async def sendMessage(self, text: str):
        for chat_room_id in CHAT_ROOM_IDS:
            await self.api_base.session.send(json.dumps({
                "action": "sendMessage",
                "text": text,
                "imagePaths": [],
                "chatRoomId": chat_room_id,
                "clientMessageId": "some_client_msg_id"
            }))

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    logger.info(f"Received a message from {message.author.name}: {message.content}")

    if message.channel.id == TARGET_CHANNEL_ID:
        api_base = APIBase()
        try:
            await api_base.connect()
            await asyncio.sleep(1)

            non_rest = NonRest(api_base)
            await non_rest.sendMessage(message.content)

        except websockets.ConnectionClosedError:
            logger.error("Connection was closed unexpectedly. Trying to reconnect...")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        finally:
            await api_base.disconnect()

    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)
