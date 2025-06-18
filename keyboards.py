from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import types

main_page_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="AI CHAT"),
            types.KeyboardButton(text="AI IMAGE"),
            types.KeyboardButton(text="Close"),
            types.KeyboardButton(text="Make an order")
        ],
        [
            types.KeyboardButton(text="WEATHER"),
            types.KeyboardButton(text="QUESTIONNAIRE")
        ]
    ],
    resize_keyboard = True
)


inline_keyboard_AI_CHAT = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="✋",callback_data="hile"),
            types.InlineKeyboardButton(text="🖕",callback_data="f off"),
        ],
    ]
)

inline_keyboard_AI_IMAGE = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="🍉", callback_data="well well well"),
            types.InlineKeyboardButton(text="🪙", callback_data="it's just an image you little jewish"),
        ]
    ]
)

inline_keyboard_Make_AN_ORDER = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="", callback_data=""),

        ]
    ]
)