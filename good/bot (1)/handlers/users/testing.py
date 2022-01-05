from aiogram.dispatcher.filters import Command
from states import Test
from aiogram.dispatcher.storage import FSMContext
from loader import dp
from aiogram import types

@dp.message_handler(Command("test"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы запустили бота.\n"
                             "Вопрос №1. \n\n"
                             "Какую криптовалюту вы бы хотели получить?")

    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer("""Вопрос №2. \n\n
                            Какое количество криптовалюты вы бы хотели получить?""")

    await Test.Q2.set()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer2=answer)

    await message.answer("""Вопрос №3. \n\n 
                        Какой валютой вы будете платить?""")

    await Test.Q3.set()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
        data = await state.get_data()

        answer1 = data.get("answer1")
        answer2 = data.get("answer2")
        answer3 = message.text

        await message.answer("Спасибо за ваши ответы, ваша заявка на рассмотрении.")
        await message.answer(f"Вы хотите {answer2} {answer1}")
        await message.answer(f"Будете платить {answer3}")

        await state.reset_state()