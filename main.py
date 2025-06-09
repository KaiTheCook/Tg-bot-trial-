import os
import asyncio

from aiogram import Bot, Dispatcher, F

from aiogram.types import Message, BotCommand, CallbackQuery
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

import keyboards as kb


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


@dp.message(F.text)
async def message_handler(message: Message):
    if message.text == "AI CHAT":
        await message.answer("Пока что в режиме разработки",reply_markup=kb.inline_keyboard_AI_CHAT)

    elif message.text == "AI IMAGE":
        await message.answer("Пока что в режиме ожидания",reply_markup=kb.inline_keyboard_AI_IMAGE )
    else:
        await message.answer(f"you typed {message.text}")


@dp.message(F.photo)
async def photo_handler(message: Message):
    await message.reply('nice photo')

async def main():
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())