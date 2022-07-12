from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp


class FSMadmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    await FSMadmin.photo.set()
    await message.reply('Загрузи фото')


@dp.message_handler(content_types=['photo'], state=FSMadmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMadmin.next()
    await message.reply("Теперь введи название")


@dp.message_handler(state=FSMadmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMadmin.next()
    await message.reply("Введи описание")


@dp.message_handler(state=FSMadmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMadmin.next()
    await message.reply("Теперь укажи цену")


@dp.message_handler(state=FSMadmin.description)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'])
