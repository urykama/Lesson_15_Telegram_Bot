import pprint

from main import bot, dp
from aiogram.types import Message
from config import admin_id


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler(commands='start')
async def echo(message: Message):
    '''
    - /start - приветствие нового пользователя
    :param message:
    :return:
    '''
    # print(message.from_user.first_name)
    text = f"{message.from_user.first_name}! Мы тебя ждали!"
    await bot.send_message(chat_id=message.from_user.id, text=text)
    # await message.answer(text=text)

@dp.message_handler(commands='help')
async def echo(message: Message):
    '''
    - /help - помощь по командам и описание системы
    :param message:
    :return:
    '''
    text = f"{message.from_user.first_name} Спасение утопающих дело рук самих утопающих Этот бот создан в учебных целях"
    await bot.send_message(chat_id=message.from_user.id, text=text)




# @bot.message_handler(commands=['start', 'help'])
# async def send_welcome(message):
#     await bot.reply_to(message, "Howdy, how are you doing?")

# <Message
#   {"message_id": 60,
#     "from":{
#       "id": 1001129070,
#         "is_bot": false,
#         "first_name": "Ural",
#         "last_name": "Kamaletdinov",
#         "username": "Ural_Kama_AD",
#         "language_code": "ru"
#     },
#           "chat": {"id": 1001129070, "first_name": "Ural", "last_name": "Kamaletdinov", "username": "Ural_Kama_AD", "type": "private"},
#           "date": 1654198648,
#           "text": "/start",
#           "entities": [{"type": "bot_command", "offset": 0, "length": 6}]}>

