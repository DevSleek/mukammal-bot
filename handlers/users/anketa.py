from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personaldata import PersonalData

@dp.message_handler(Command("anketa"), state=None)
async def enter_test(message: types.message):
    await message.answer('Enter your fullname')
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {
            "name": fullname
        }
    )

    await message.answer('Enter your email address')
    await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.message, state: FSMContext):
    email = message.text

    await state.update_data(
        {
            "email": email
        }
    )

    await message.answer('Enter your phone number')
    await PersonalData.next()

@dp.message_handler(state=PersonalData.phone)
async def answer_email(message: types.message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            "phone": phone
        }
    )

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = 'The following information has been received:\n'
    msg += f'Your name - {name}\n'
    msg += f'Your email - {email}\n'
    msg += f'Your phone: - {phone}\n'
    await message.answer(msg)
    await state.finish()
    # await state.reset_sate()




