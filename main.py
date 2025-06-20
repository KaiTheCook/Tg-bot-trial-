import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from aiogram.types import Message, BotCommand, CallbackQuery, ReplyKeyboardRemove

from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

import keyboards as kb
from db_interaction import db
import service as service
from states import Questionnaire

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

TOKEN =os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

commands = [
    BotCommand(command="start",description='start using this bot'),
    BotCommand(command="help",description="ask for a help"),
    BotCommand(command="info",description="list of commands")
]

@dp.callback_query()
async def get_callback(callback: CallbackQuery):
    logging.info(f"Callback {callback.data} от {callback.from_user.id}")
    await callback.message.edit_reply_markup(reply_markup=None)


    if callback.data == "hile":
        await callback.message.answer('Hile!')
    elif callback.data == "f off":
        await callback.message.answer('F OFF!')
    elif callback.data == "well well well":
        await callback.message.answer("WELL🍉 WELL🏀 WELL🐓")
    elif callback.data == "it's just an image you little jewish":
        await callback.message.answer("gotcha!try to steal this coin you vile jew")


@dp.message(CommandStart())
async def start_command(message: Message):
    logging.info(f"Пользователь {message.from_user.id} начал бота")
    await message.answer("Hello i'm ur 1st bot",reply_markup= kb.main_page_keyboard )


@dp.message(Command('help'))
async def help_command(message: Message):
    await message.reply("Ask me if you need any help")


@dp.message(Command('info'))
async def info_command(message: Message):
    commands_text = (
        "list of commands:\n"
        "Start\n"
        "help\n"
        "info\n"
    )
    await message.answer(commands_text)



@dp.message()
async def message_handler(message: Message,state: FSMContext):
    current_state = await state.get_state()
    user = await db.check_user(message.chat.id)
    if user is None:
        await db.add_user(message.chat.id, message.from_user.username)
    if current_state is not None:
        await service.handle_questionnaire(message,state)
    else:
        if message.text == "AI CHAT":
            await message.answer("Пока что в режиме разработки",reply_markup=kb.inline_keyboard_AI_CHAT)

        elif message.text == "AI IMAGE":
            await message.answer("Пока что в режиме ожидания",reply_markup=kb.inline_keyboard_AI_IMAGE )
        elif message.text == "close":
            await message.answer("Keyboard is closed",reply_markup=ReplyKeyboardRemove())
        elif message.text == "QUESTIONNAIRE":
            await state.set_state(Questionnaire.gender)
            await message.answer("Какой у тебя пол?")
        elif message.text == "WEATHER":
            await service.handle_weather(message)
        else:
            await service.chat_with_ai(message)


@dp.message(F.photo)
async def photo_handler(message: Message):
    await message.reply('nice photo')

async def main():
    await bot.set_my_commands(commands)
    try:
        print("Bot started")
        await db.connect()
        await dp.start_polling(bot)
    except Exception as e:
        print(e)
    finally:
        await db.disconnect()


if __name__ == '__main__':
    asyncio.run(main())