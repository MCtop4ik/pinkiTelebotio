from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboard import kb_client
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(commands=['start', 'help'])
async def commandsStart(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Здрасте, я ожил", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: https://t.me/zetnisbot')


@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Здрасте, я ожил", reply_markup=ReplyKeyboardRemove())
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: https://t.me/zetnisbot')


def registerHandlersClient(disp: Dispatcher):
    disp.register_message_handler(commandsStart, commands=['start', 'help'])
    disp.register_message_handler(reply, commands=['reply'])

