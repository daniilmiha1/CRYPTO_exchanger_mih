from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')

@dp.message_handler(content_types = ["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact"])
async def get_audio(message):
    await dp.bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)

