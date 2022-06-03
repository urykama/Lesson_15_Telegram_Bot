from aiogram import executor, Dispatcher, Bot  # , types
# from bs4 import BeautifulSoup
import asyncio
from config import BOT_TOKEN
from main_hh import HH

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
hh = HH()
print(hh)
text = '' + str(hh)
print(type(text))

if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)