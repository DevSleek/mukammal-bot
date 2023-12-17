from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.personaldata import PersonalData

from loader import dp


@dp.message_handler(CommandHelp(), state=PersonalData.fullname)
async def bot_help(message: types.Message):
    text = (
        'Ism va familiyangizni kiriting, iltimos'
    )
    
    await message.answer(text)