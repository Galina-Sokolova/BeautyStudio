import setting_commands
from aiogram import Bot, executor, dispatcher, Dispatcher, types

from keyboards import *
from config import TOKEN_BOT

bot = Bot(TOKEN_BOT)
dp = Dispatcher(bot)


async def on_startup(_):
    print('БОТ ЗАПУЩЕН!!!')
    await setting_commands.set_default_commands(bot)


@dp.message_handler(commands=['start'])
# Навешиваем обработчик, который будет давать функции start_command реагировать только на сообщение start
async def start_command(message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=open('resoursers/images/start.jpg', 'rb'),
                         caption='Добро пожаловать в нашу студию',
                         reply_markup=ikb_start)
    await message.delete()


@db.callback_query_handler(text='Запись на прием')
async def register_to_master(callback):  # эта функция запустит функцию start_FSM(db) из user.py
    start_FSM(db)


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup
    )
