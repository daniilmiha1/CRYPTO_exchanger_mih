from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать работу',
        '/help - Получить помощь',
        '/about - Получить информацию про нас',
        '/language - Изменить язык',
        '/test - Купить криптовалюту',
        'Выберите нужную вам команду для работы с ботом.',
        'При возникновении вопросов, обращайтесь в службу поддержки пользователей @businamih'
    ]
    await message.answer('\n'.join(text))