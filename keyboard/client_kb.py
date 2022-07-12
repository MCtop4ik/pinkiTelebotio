from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/help')
b2 = KeyboardButton('/reply')
b3 = KeyboardButton('Поделиться номером', request_contact=True)
b4 = KeyboardButton('Отправить, где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).insert(b2).add(b3).add(b4)
