from aiogram import types, Dispatcher
from create_bot import dp


@dp.message_handler()
async def echo_send(message: types.Message):
    #    await message.answer(message.text) # шлет сообщение
    #    await message.reply(message.text)  # с отсылкой на команду или сообщение
    #   await bot.send_message(message.from_user.id, message.text) Пишет пользователю в личку
    if message.text == 'Привет':
        await message.reply('Хай')


def registerHandlersOther(disp: Dispatcher):
    disp.register_message_handler(echo_send)
