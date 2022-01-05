from loader import dp
from aiogram import types

@dp.message_handler(text="Михальков")
async def one_two_three(message: types.Message):
    await message.answer(text="Красава, знаешь батю")