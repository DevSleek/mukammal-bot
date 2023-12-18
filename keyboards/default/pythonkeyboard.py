from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menupython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#00 Kirish'),
            KeyboardButton(text='#01 Kerakli dasturlar'),
            KeyboardButton(text='#02 Hello world!'),
        ],
        [
            KeyboardButton(text='Ortga'),
            KeyboardButton(text='Boshiga'),
        ],
    ],
    resize_keyboard=True
)
