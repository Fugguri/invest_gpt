
import json
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from my_json import Json_worker
from openai import OpenAI
import asyncio
from bd import Database
from channel_joined import ChannelJoinedMiddleware
js = Json_worker("config.json")
config = js.get_config()
TOKEN_API = config["TOKEN_API"]
OPENAI_KEY = config["openai_key"]


users_message = {}
channels = config["channels"]
storage = MemoryStorage()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
bot = Bot(TOKEN_API, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage, loop=loop)
db = Database("gpt.db")


async def on_startup(_):
    print("Бот запущен")
    dp.middleware.setup(ChannelJoinedMiddleware(js=js))
    db.cbdt()


async def on_shutdown(_):
    print("Бот остановлен")


if __name__ == "__main__":

    from handlers import *
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
