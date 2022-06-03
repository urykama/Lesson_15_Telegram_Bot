import pprint
from main import bot, dp, hh
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


@dp.message_handler(commands='hh')
async def echo(message: Message):
    '''
    - /help - помощь по командам и описание системы
    :param message:
    :return:
    '''

    await bot.send_message(chat_id=message.from_user.id, text='вывод настроек')
    print('вывод настроек')
    text = str(hh)
    await bot.send_message(chat_id=message.from_user.id, text=text)

@dp.message_handler(commands='search')
async def echo(message: Message):
    '''
    - /help - помощь по командам и описание системы
    :param message:
    :return:
    '''
    await bot.send_message(chat_id=message.from_user.id, text='Идёт поиск: пожалуйста подождите...')
    print('запущен поиск')
    print(hh.search())
    text = str(hh.search())
    await bot.send_message(chat_id=message.from_user.id, text=text)


