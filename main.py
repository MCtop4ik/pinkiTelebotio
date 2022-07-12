from aiogram.utils import executor
from create_bot import dp
from handlers import client, other


async def on_startup(_):
    print("Бот вышел онлайн")


client.registerHandlersClient(disp=dp)
other.registerHandlersOther(disp=dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
